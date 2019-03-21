CGC:

cgc binaries unpatched and patched
https://github.com/zardus/cgc-bins

build scripts to build CGC binaries as Linux binaries for different operating systems.
It is loosely based on TrailOfBits' cb-multios.
https://github.com/zardus/cgc-multiarch


Windows:

Trying to use on windows style executables
Also could look at the msvc compiler generated binaries

binutils, coreutils, findutils for windows

* UnxUtils
    * http://unxutils.sourceforge.net/

* GNUWin32
    * http://gnuwin32.sourceforge.net/packages/coreutils.htm
    * http://gnuwin32.sourceforge.net/packages/binutils.htm
    * http://gnuwin32.sourceforge.net/packages/findutils.htm

* MinGW32
    * https://sourceforge.net/projects/mingw/files/MinGW/Base/binutils/

Different executable types

for f in $(ls) ; do file $f; done

binutils, coreutils, findutils
all striped binaries
PE32 executable (console) Intel 80386 (stripped to external PDB), for MS Windows

UnxUtils
mostly non stripped, one is compressed
PE32 executable (console) Intel 80386, for MS Windows
PE32 executable (console) Intel 80386, for MS Windows, UPX compressed
PE32 executable (console) Intel 80386 (stripped to external PDB), for MS Windows


