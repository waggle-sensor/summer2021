import cv2

from main import find_mean_hsv  # from file import function
from main import find_standard_deviation_hsv
import unittest

# I am able to run test through command line, but not on pycharm, I need to fix that
# run test through command line "python -m unittest test.py"
class Test(unittest.TestCase):

    # Add more tests with different solid colors
    # Generate a random x, y spot instead of picking it yourself randomly
    def test_mean_hue(self):
        file_path = 'test_images/Color-blue.jpg'
        test_image = cv2.imread(file_path, 1)
        hsv_test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2HSV)

        mean_hue_actual = find_mean_hsv(hsv_test_image)[0]
        mean_hue_expected = hsv_test_image[25, 100, 0]

        self.assertEqual(mean_hue_actual ,mean_hue_expected)

    def test_mean_sat(self):
        file_path = 'test_images/Color-blue.jpg'
        test_image = cv2.imread(file_path, 1)
        hsv_test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2HSV)

        mean_sat_actual = find_mean_hsv(hsv_test_image)[1]
        mean_sat_expected = hsv_test_image[24, 104, 1]

        self.assertEqual(mean_sat_actual, mean_sat_expected)

    def test_mean_val(self):
        file_path = 'test_images/Color-blue.jpg'
        test_image = cv2.imread(file_path, 1)
        hsv_test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2HSV)

        mean_val_actual = find_mean_hsv(hsv_test_image)[1]
        mean_val_expected =  hsv_test_image[99, 40, 2]

        self.assertEqual(mean_val_actual, mean_val_expected)

    def test_SD_hue_zero(self):
        file_path = 'test_images/Color-blue.jpg'
        test_image = cv2.imread(file_path, 1)
        hsv_test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2HSV)

        SD_hue_actual = find_standard_deviation_hsv(hsv_test_image)[0]
        SD_hue_expected = 0

        print(SD_hue_actual)

        self.assertEqual(SD_hue_actual, SD_hue_expected)

    def test_SD_sat_zero(self):
        file_path = 'test_images/Color-blue.jpg'
        test_image = cv2.imread(file_path, 1)
        hsv_test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2HSV)

        SD_sat_actual = find_standard_deviation_hsv(hsv_test_image)[1]
        SD_sat_expected = 0

        print(SD_sat_actual)

        self.assertEqual(SD_sat_actual, SD_sat_expected)

    def test_SD_val_zero(self):
        file_path = 'test_images/Color-blue.jpg'
        test_image = cv2.imread(file_path, 1)
        hsv_test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2HSV)

        SD_val_actual = find_standard_deviation_hsv(hsv_test_image)[2]
        SD_val_expected = 0

        print(SD_val_actual)

        self.assertEqual(SD_val_actual, SD_val_expected)

    # can use high contrast images for SD

    def test_SD_val_compare(self):

        '''
            instead of finding images with different contrasts,
            use one image and change the contrast of the image many times
            and compare all those values
        '''

        file_path = 'test_images/black_and_white_checker.jpg'
        test_image = cv2.imread(file_path, 1)
        hsv_test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2HSV)

        # I can compare SD instead of finding exact ones
        SD_val_high = find_standard_deviation_hsv(hsv_test_image)[2]
        SD_val_medium = 40
        SD_val_low = 0

        print(SD_val_high)
        print(SD_val_medium)
        print(SD_val_low)

        result = False

        if (SD_val_high > SD_val_medium > SD_val_low):
            result = True

        self.assertEqual(result, True)


