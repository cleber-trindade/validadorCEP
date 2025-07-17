<h1>CEP Validator</h1>
<h2>Description</h2>
This project is an API developed with Flask. It allows you to retrieve full address information using a Brazilian ZIP code (CEP).
It is intended for educational purposes only, to demonstrate how to consume a real API and handle errors properly.

<h2>1. Cloning the Repository</h2>
First, you need to clone the repository to access and run the project:

```
git clone (https://github.com/cleber-trindade/validadorCEP.git)
```
<h2>Creating a Virtual Environment (Optional, but Recommended)</h2>
It's recommended to use a virtual environment to isolate dependencies.

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
<h2>3. Installing Dependencies </h2>
Install the required packages using:

```
pip install -r requirements.txt
```

<h2>Running the Application</h2>
You can star the app with:

```
python app.py 
```
If it works correctly, you should see this message in the terminal:

```
Running on http://127.0.0.1:5000
```
<h2>Option 1 – Using Postman</h2>
Open Postman and create a GET request with this URL:

```
http://127.0.0.1:5000/cep/01001000
```

Replace 01001000 with any valid Brazilian CEP (ZIP code).
The response will include full address data from the ViaCEP API.

<h3>If the CEP is invalid or does not exist:</h3>

http://127.0.0.1:5000/cep/abcdefg → returns 400 (Invalid CEP)
http://127.0.0.1:5000/cep/00000000 → returns 404 (CEP not found)

<h2>Option 2 – Using the Browser</h2>
You can also test it by typing the full URL directly in your browser:

```
http://127.0.0.1:5000/cep/01001000
```
<h1>5. Requirements and Acceptance Criteria</h1>
<h2>Requirements</h2>

<ul>
<li>Accept a ZIP code (CEP) as input via URL</li>
<li>Return full address data using the ViaCEP public API</li>
<li>Handle errors for invalid or non-existent ZIP codes</li>
</ul>

<h2>Acceptance Criteria</h2>
<ul>
<li>Valid ZIP code returns HTTP 200 with address data</li>
<li>Invalid ZIP code (letters, wrong format) returns HTTP 400</li>
<li>Non-existent ZIP code returns HTTP 404</li>
</ul>

<h1>Dependences</h1>
Install all required dependences using:

```
pip install flask requests
```
