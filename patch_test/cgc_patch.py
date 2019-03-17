import patcherex
from patcherex.backends.detourbackend import DetourBackend
from patcherex.backends.reassembler_backend import ReassemblerBackend
from patcherex.patches import *

# the detour backend can be used as well:
# backend = DetourBackend("test_binaries/CADET_00003")
backend = ReassemblerBackend("cgc_binaries/CADET_00003")
patches = []

transmit_code = '''
  ; eax is the transmitted buffer
  ; ebx is the length
  pusha
  mov ecx,eax
  mov edx,ebx
  mov eax,0x2
  mov ebx,0x1
  mov esi,0x0
  int 0x80
  popa
  ret
  '''

patches.append(AddCodePatch(transmit_code, name="transmit_function"))
patches.append(AddRODataPatch(b"HI!\x00", name="transmitted_string"))

# the following code is going to be executed just before the original instruction at 0x8048166
injected_code = '''
; at this code location, it is fine to clobber eax and ebx
mov eax, {transmitted_string} ; a patch can refer to another patch address, by putting its name between curly brackets
mov ebx, 4
call {transmit_function}
'''

patches.append(InsertCodePatch(0x8048166,injected_code,name="injected_code_after_receive"))

# now we ask to the backend to inject all our patches
backend.apply_patches(patches)

# and then we save the file
backend.save("/tmp/CADET_00003_mod1")
# at this point you can try to run /tmp/CADET_00003_mod1 inside the DECREE VM or using our modified version of QEMU

