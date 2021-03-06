from platformcommon import PlatformCommon
import os

class PlatformCommodore(PlatformCommon):
    def run(self):
        d64s = self.find_files_with_extension('d64')
        prgs = self.find_files_with_extension('prg')

        if len(d64s) == 0:
            d64s = self.find_d64_files()

        if len(d64s) == 0 and len(prgs) == 0:
            print("Didn't find any d64 or prg files.")
            exit(-1)

        runcommand = ['x64']
        runcommand.append('-fullscreen')

        flipfile = self.datadir + "/fliplist.vfl"
        with open(flipfile, "w") as f:
            f.write("UNIT 8\n")
            for disk in d64s:
                f.write(disk + "\n")

        if len(d64s) > 0:
            d64s = self.sort_disks(d64s)
            runcommand = runcommand + ['-flipname', flipfile, d64s[0]]

        if len(prgs) > 0:
            runcommand.append(prgs[0])

        self.run_process(runcommand)

    def supported_platforms(self):
        return ['commodore64']

# Tries to identify d64 files by any magic necessary
    def find_d64_files(self):
        d64_files = []
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size == 174848: # All d64:s seem to be this size..
                d64_files.append(file)
        return d64_files
