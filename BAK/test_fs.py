import unittest
from FileSystem import FileSystem
#from FileSystem import get_name

class FileSystemTest(unittest.TestCase):

    def setUp(self):
        cmsfolderpath = "/home/huy/foldermon"
        self.fs = FileSystem(cmsfolderpath)

    def test_get_name(self):≡jedi=0, ≡             () ≡jedi≡
        self.assertEqual(self.fs.get_name(), "foldermon")



if __name__ == '__main__':
    unittest.main()
