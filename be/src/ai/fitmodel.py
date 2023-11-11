# Import the libraries we will be using
import numpy as np

# Data dictionary
world_price = {
    "stainless steel hc304": [
        [3393, 3309, 3313, 3221, 3380, 3534, 3636, 3427, 3264, 3184, 3046],
        "https://mepsinternational.com/gb/en/products/world-steel-prices",
    ],
    "stainless steel hc316": [
        [4746, 4584, 4632, 4615, 4874, 5306, 5712, 5521, 5169, 4850, 4647],
        "https://mepsinternational.com/gb/en/products/world-steel-prices",
    ],
    "stainless steel hr304": [
        [3969, 4042, 3994, 3803, 3996, 4154, 4193, 3980, 3814, 3743, 3576],
        "https://mepsinternational.com/gb/en/products/world-steel-prices",
    ],
    "stainless steel hr316": [
        [5434, 5469, 5449, 5238, 5513, 5952, 6342, 6081, 5707, 5379, 5167],
        "https://mepsinternational.com/gb/en/products/world-steel-prices",
    ],
    "stainless steel cr304": [
        [3618, 3509, 3512, 3417, 3576, 3729, 3823, 3660, 3473, 3386, 3235],
        "https://mepsinternational.com/gb/en/products/world-steel-prices",
    ],
    "stainless steel cr316": [
        [5018, 4823, 4871, 4860, 5119, 5557, 5958, 5803, 5428, 5101, 4883],
        "https://mepsinternational.com/gb/en/products/world-steel-prices",
    ],
    "stainless steel cr430": [
        [2240, 2195, 2190, 2038, 2048, 2089, 2144, 2095, 2074, 2056, 1972],
        "https://mepsinternational.com/gb/en/products/world-steel-prices",
    ],
    "stainless steel bd304": [
        [4890, 4684, 4674, 4423, 4650, 4819, 5000, 4787, 4549, 4517, 4426],
        "https://mepsinternational.com/gb/en/products/world-steel-prices",
    ],
    "stainless steel bd316": [
        [6388, 6140, 6153, 6016, 6335, 6662, 7076, 7023, 6632, 6288, 6156],
        "https://mepsinternational.com/gb/en/products/world-steel-prices",
    ],
    "nickel": [
        [12500, 12500, 15500, 15500, 12500, 12000, 14000, 17000, 18500, 18250, 19000, 19900, 25000, 28500, 22500, 25000, 26000, 23500, 21000],
        "Nickel London Metal Exchange (LME) Nickel Cash Official",
    ],
}


# Fit the model using linear regression with mean-squared error
def fitModel(material):
    data = world_price[material][0]
    # Stack the coefficient into a matrix
    A = np.vstack([np.linspace(0, len(data) - 1, len(data)), np.ones(len(data))]).T
    # Fit the coefficient using numpy.linalg.lstsq
    m, c = np.linalg.lstsq(A, data, rcond=None)[0]
    return m, c


def predict(material, time, unit):
    # Adjust the time based on the input unit
    if unit == "year":
        time = 12 * time
    elif unit == "day":
        time = time / 30
    # Coefficient of the fitted model
    a, b = fitModel(material)
    # Return the predicted value
    return a * (time + 11) + b, world_price[material][1]
