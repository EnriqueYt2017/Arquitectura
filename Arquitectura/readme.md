pip install -r requirements.txt

Utilizaremos para el correo el host de mailtrap

<!-- PAYPAL -->
<!-- 
https://sandbox.paypal.com

cliente id:
AU3OWDXbWSMlfCscxGPeb1ni-9DOoaBCJBFZja8rI52y5CHWHBcJ4fTrdzTKctJGTCGmDFOk2fHRdgNj


tienda:
sb-cvvle30686372@business.example.com
t4MM*x6r

personal:
sb-pzvx231405988@personal.example.com
Qt%H[9kw 
-->

python -m aiosmtpd -n -l localhost:8025