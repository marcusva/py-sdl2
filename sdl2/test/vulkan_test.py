import unittest
from sdl2 import SDL_Init, SDL_Quit, SDL_INIT_VIDEO
from sdl2 import vulkan

class TestSDLVulkan(unittest.TestCase):
    __tags__ = ["sdl"]

    @classmethod
    def setUpClass(cls):
        if SDL_Init(SDL_INIT_VIDEO) != 0:
            raise unittest.SkipTest('Video subsystem not supported')

    @classmethod
    def tearDownClass(cls):
        SDL_Quit()

    @unittest.skip("not implemented")
    def test_SDL_Vulkan_LoadLibrary(self):
        pass

    @unittest.skip("not implemented")
    def test_SDL_Vulkan_GetVkGetInstanceProcAddr(self):
        pass

    @unittest.skip("not implemented")
    def test_SDL_Vulkan_UnloadLibrary(self):
        pass

    @unittest.skip("not implemented")
    def test_SDL_Vulkan_GetInstanceExtensions(self):
        pass

    @unittest.skip("not implemented")
    def test_SDL_Vulkan_CreateSurface(self):
        pass

    @unittest.skip("not implemented")
    def test_SDL_Vulkan_GetDrawableSize(self):
        pass
