# O365DomScan

O365DomScan is a Python script designed to identify and list domains related to a given domain within the Office 365 environment.

## Features

- Fetch related domains for a specified Office 365 domain.
- Easy to use and configure.

## Requirements

- Python 3.x
- pipx

## Installation

1. pipx:

   ```sh
   pipx install git+https://github.com/phor3nsic/O365DomScan.git
   ```

## Usage

1. Open the script and configure the main domain you want to scan.

2. Run the script:

   ```sh
   O365domscan example.com
   ```

3. The script will output a list of related domains.


## Example

Here is an example of how to use O365DomScan:

```sh
O365domscan example.com
```

Output:
```
Related domains for example.com:
- backofficeexample.com
- anotherexample.com
- ...
```

## Contributing

Feel free to fork this project, create a branch, and submit a pull request with your improvements.

## License

This project is licensed under the MIT License.