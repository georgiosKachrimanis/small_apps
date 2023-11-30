# Amazon Price Alert

This script is designed to monitor the price of a specific product on Amazon and send an email alert if the price drops below a predetermined threshold.

## Features

- **Product URL Monitoring:** Set the specific Amazon product URL to monitor.
- **Price Alert:** Receive an email alert if the product's price drops below your set threshold.
- **Flexible Configuration:** Uses environment variables for sensitive information.

## Setup

1. **Environment Variables:** Set your email credentials and SMTP server details as environment variables.
2. **Dependencies:** Install the required Python libraries with `pip install -r requirements.txt`.
3. **Run the Script:** Execute the script to start monitoring the product price.

## Usage

- Update the `product_url` variable in the script with the specific Amazon product URL you want to monitor.
- Set the `alert_price` in the `main` function to your desired threshold.

## Contributing

Feel free to fork this repository and contribute by submitting a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
