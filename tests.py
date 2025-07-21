from solution import discount_prices_list, discount_prices_numpy
import numpy as np

def test_discount_prices_list_and_numpy():
    # Test: Applying discount to a list of prices
    prices_list = [100, 200, 300, 400]
    expected_discounted_list = [90.0, 180.0, 270.0, 360.0]  # 10% discount applied
    expected_discounted_array = np.array([90.0, 180.0, 270.0, 360.0])  # Expected NumPy array result

    # Test List-based approach
    discounted_list = discount_prices_list(prices_list)
    try:
        assert discounted_list == expected_discounted_list, f'Expected {expected_discounted_list}, but got {discounted_list}'
        print('✅ Test Passed: List-based discount applied correctly.')
    except Exception as e:
        print(f'❌ Test Failed: {e}')

    # Test NumPy-based approach
    discounted_array = discount_prices_numpy(np.array(prices_list))
    try:
        assert np.array_equal(discounted_array, expected_discounted_array), f'Expected {expected_discounted_array}, but got {discounted_array}'
        print('✅ Test Passed: NumPy-based discount applied correctly.')
    except Exception as e:
        print(f'❌ Test Failed: {e}')

# Call the test function to run the tests
test_discount_prices_list_and_numpy()

