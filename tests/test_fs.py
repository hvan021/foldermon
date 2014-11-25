import unittest
from foldermon.filesystem import FileSystem

class FileSystemTest(unittest.TestCase):

    def setUp(self):
        cmsfolderpath =  "/home/huy/foldermon"
        self.fs =  FileSystem(cmsfolderpath)

    def test_get_name(self):
        self.assertTrue(self.fs.get_name(), "foldermon")

    def test_checksum_folder(self):
        self.assertEqual(self.fs.checksum(), None)

    def test_checksum_file(self):
        samplefile = FileSystem('/home/huy/foldermon/README.md')
        self.assertEqual(samplefile.checksum(), 'd52e8465c127ebb335dce2660d4d65f8')

#if __name__ == '__main__':
    #unittest.main()
