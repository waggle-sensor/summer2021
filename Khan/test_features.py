import cv2

from detect_features import find_mean_hsv
from detect_features import find_standard_deviation_hsv
from detect_features import find_edge_density
from detect_features import find_straight_edge_density
from detect_features import find_entropy
import unittest


def convert_file_to_image(file_path):

    test_image = cv2.imread(file_path, 1)
    hsv_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2HSV)

    return [hsv_image, test_image]

# I am able to run test through command line, but not on pycharm, I need to fix that
# run test through command line "python -m unittest test_features.py"
class Test(unittest.TestCase):

    # Add more tests with different solid colors
    # Generate a random x, y spot instead of picking it yourself randomly
    def test_mean_hue1(self):
        hsv_test_image = convert_file_to_image('test_images\Color-blue.jpg')[0]

        mean_hue_actual = find_mean_hsv(hsv_test_image)[0]
        mean_hue_expected = hsv_test_image[25, 100, 0]

        self.assertEqual(mean_hue_actual ,mean_hue_expected)

    def test_mean_hue2(self):
        hsv_test_image = convert_file_to_image('test_images\diff_shades_red.png')[0]

        hue_mean = find_mean_hsv(hsv_test_image)[0]

        result = False

        if ((hue_mean >= 0 and hue_mean <= 20) or (hue_mean >= 160 and hue_mean <= 180)):
            result = True

        print("Hue mean:", hue_mean)

        self.assertEqual(result, True)

    def test_mean_sat(self):
        hsv_test_image = convert_file_to_image('test_images/Color-blue.jpg')[0]

        mean_sat_actual = find_mean_hsv(hsv_test_image)[1]
        mean_sat_expected = hsv_test_image[24, 104, 1]

        self.assertEqual(mean_sat_actual, mean_sat_expected)

    def test_mean_val(self):
        hsv_test_image = convert_file_to_image('test_images/Color-blue.jpg')[0]

        mean_val_actual = find_mean_hsv(hsv_test_image)[1]
        mean_val_expected = hsv_test_image[99, 40, 2]

        self.assertEqual(mean_val_actual, mean_val_expected)

    def test_SD_hue_zero(self):
        hsv_test_image = convert_file_to_image('test_images/Color-blue.jpg')[0]

        SD_hue_actual = find_standard_deviation_hsv(hsv_test_image)[0]
        SD_hue_expected = 0

        self.assertEqual(SD_hue_actual, SD_hue_expected)

    def test_SD_sat_zero(self):
        hsv_test_image = convert_file_to_image('test_images/Color-blue.jpg')[0]

        SD_sat_actual = find_standard_deviation_hsv(hsv_test_image)[1]
        SD_sat_expected = 0

        self.assertEqual(SD_sat_actual, SD_sat_expected)

    def test_SD_val_zero(self):
        hsv_test_image = convert_file_to_image('test_images/Color-blue.jpg')[0]

        SD_val_actual = find_standard_deviation_hsv(hsv_test_image)[2]
        SD_val_expected = 0

        self.assertEqual(SD_val_actual, SD_val_expected)

    def test_SD_val_compare(self):

        hsv_test_black_white = convert_file_to_image('test_images/black_and_white_checker.jpg')[0]
        hsv_test_black_light_grey = convert_file_to_image('test_images/black_lightGrey.jpg')[0]
        hsv_test_black_dark_grey = convert_file_to_image('test_images/black_darkGrey.jpg')[0]

        # I can compare SD instead of finding exact ones
        SD_val_high = find_standard_deviation_hsv(hsv_test_black_white)[2]
        SD_val_medium = find_standard_deviation_hsv(hsv_test_black_light_grey)[2]
        SD_val_low = find_standard_deviation_hsv(hsv_test_black_dark_grey)[2]

        result = False

        if (SD_val_high > SD_val_medium > SD_val_low):
            result = True

        self.assertEqual(result, True)

    def test_SD_hue(self):

        hsv_test_image_red_green = convert_file_to_image('test_images/red_green.jpg')[0]
        hsv_test_image_red_yellow = convert_file_to_image('test_images/red_yellow.png')[0]
        hsv_test_image_two_green = convert_file_to_image('test_images/two_green.jpg')[0]

        SD_hue_high = find_standard_deviation_hsv(hsv_test_image_red_green)[0]
        SD_hue_medium = find_standard_deviation_hsv(hsv_test_image_red_yellow)[0]
        SD_hue_low = find_standard_deviation_hsv(hsv_test_image_two_green)[0]

        result = False

        if (SD_hue_high > SD_hue_medium > SD_hue_low):
            result = True

        self.assertEqual(result, True)

    def test_SD_hue_gradient(self):

        hsv_test_yellow_purple = convert_file_to_image('test_images/yellow_purple_gradient.png')[0]
        hsv_test_purple_blue = convert_file_to_image('test_images/Purple_Blue_gradient.jpg')[0]
        hsv_test_image_purple = convert_file_to_image('test_images/purple_gradient.png')[0]

        SD_hue_high = find_standard_deviation_hsv(hsv_test_yellow_purple)[0]
        SD_hue_medium = find_standard_deviation_hsv(hsv_test_purple_blue)[0]
        SD_hue_low = find_standard_deviation_hsv(hsv_test_image_purple)[0]

        result = False

        if (SD_hue_high > SD_hue_medium > SD_hue_low):
            result = True

        self.assertEqual(result, True)

    def test_SD_sat(self):

        hsv_test_high_to_low_sat = convert_file_to_image('test_images/high_low_sat.png')[0]
        hsv_test_medium_sd_sat = convert_file_to_image('test_images/medium_sat.png')[0]
        hsv_test_low_sd_sat = convert_file_to_image('test_images/low_sd_sat.png')[0]

        SD_sat_high = find_standard_deviation_hsv(hsv_test_high_to_low_sat)[1]
        SD_sat_medium = find_standard_deviation_hsv(hsv_test_medium_sd_sat)[1]
        SD_sat_low = find_standard_deviation_hsv(hsv_test_low_sd_sat)[1]

        result = False

        if (SD_sat_high > SD_sat_medium > SD_sat_low):
            result = True

        self.assertEqual(result, True)

    def test_edge_density1(self):

        low_edge_density_image = convert_file_to_image('test_images/low_edge_density.jpg')[1]
        medium_edge_density_image = convert_file_to_image('test_images/medium_edge_density.jpg')[1]
        high_edge_density_image = convert_file_to_image('test_images/high_edge_density.png')[1]

        edge_density_low = find_edge_density(low_edge_density_image)
        edge_density_medium = find_edge_density(medium_edge_density_image)
        edge_density_high = find_edge_density(high_edge_density_image)

        result = False

        if(edge_density_low < edge_density_medium < edge_density_high):
            result = True

        self.assertEqual(result, True)

    def test_edge_density2(self):

        low_edge_density_image = convert_file_to_image('test_images/low_edge_density2.png')[1]
        medium_edge_density_image = convert_file_to_image('test_images/medium_edge_density2.png')[1]
        high_edge_density_image = convert_file_to_image('test_images/high_edge_density2.png')[1]

        edge_density_low = find_edge_density(low_edge_density_image)
        edge_density_medium = find_edge_density(medium_edge_density_image)
        edge_density_high = find_edge_density(high_edge_density_image)

        result = False

        if(edge_density_low < edge_density_medium < edge_density_high):
            result = True

        self.assertEqual(result, True)

    def test_straight_edge_density1(self):

        straight_edge_density_low = convert_file_to_image('test_images/low_edge_density.jpg')[1]
        straight_edge_density_high = convert_file_to_image('test_images/high_edge_density.png')[1]

        straight_edges_length_low = find_straight_edge_density(straight_edge_density_low)
        straight_edges_length_high = find_straight_edge_density(straight_edge_density_high)

        result = False

        if (straight_edges_length_high > straight_edges_length_low):
            result = True

        self.assertEqual(result, True)

    def test_straight_edge_density2(self):

        straight_edge_density_low = convert_file_to_image('images/image1.jpg')[1]
        straight_edge_density_high = convert_file_to_image('images/image2.jpg')[1]

        num_straight_edges_low = find_straight_edge_density(straight_edge_density_low)
        num_straight_edges_high = find_straight_edge_density(straight_edge_density_high)

        result = False

        if (num_straight_edges_high > num_straight_edges_low):
            result = True

        self.assertEqual(result, True)

    def test_entropy1(self):

        high_entropy_image = convert_file_to_image('test_images/High_entropy.png')[1]
        low_entropy_image = convert_file_to_image('test_images/red_green.jpg')[1]

        high_entropy = find_entropy(high_entropy_image)
        low_entropy = find_entropy(low_entropy_image)

        print("High entropy:", high_entropy)
        print("Low entropy:", low_entropy)

        result = False

        if (high_entropy > low_entropy):
            result = True

        self.assertEqual(result, True)

    def test_entropy2(self):

        high_entropy_image = convert_file_to_image('images/image1.jpg')[1]
        low_entropy_image = convert_file_to_image('images/image2.jpg')[1]

        high_entropy = find_entropy(high_entropy_image)
        low_entropy = find_entropy(low_entropy_image)

        result = False

        if (high_entropy > low_entropy):
            result = True

        self.assertEqual(result, True)

    def test_entropy3(self):

        entropy_zero_image = convert_file_to_image('test_images/Color-blue.jpg')[1]

        entropy_zero = find_entropy(entropy_zero_image)

        self.assertEqual(entropy_zero, 0)














