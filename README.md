This is the core API for my implementation of Drucker-Flickr, for which you'll need to build an interface to handle the responses you get.

#### The "Drucker-Flickr" Method for multiplying large numbers.

My implementation of [Andy Drucker's method](http://people.csail.mit.edu/andyd/rec_method.pdf) for multiplying large numbers without writing writing anything down (as an intermediate step anyway).  See [Scott Aarsonon's post](http://www.scottaaronson.com/blog/?p=728) for its significance in computational complexity.

The key trick behind it is this: if you have seen a picture before, you can remember *that* you have seen it, and distinguish it from ones you haven't seen.  So here's what you do:

1) Reserve (without looking at them) ten random pictures corresponding to digits 0-9.

2) Look at (only!) the one corresponding to the digit you want to "write down".

3) When you want to look up the number you've remembered this way, pull up the full 10-image block.  The one you remember tells you the digit you stored!

Then, it's just a matter of having a predictable mapping between a) blocks of images, and b) places in your multiplication workspace, so you don't have to write down which position goes with which image block.  This app will (eventually) do grunt work for you!

#### Installation and Usage

Clone the repo and set up dependencies for development using virutalenv:

    virtualenv venv
    . ./venv/bin/activate
    pip install -r requirements.txt

For Django apps: 

1. Add "DFMM-core" to your INSTALLED\_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'DFMM_core',
    )

2. Include the DFMM\_core URLconf in your project urls.py, with some namespacing for the api calls (in this example, the `/dfmm-api/` namespace)

    url(r'^dfmm-api/', include('DFMM_core.urls')),

3. Run `python manage.py migrate` to create the models

4. Send api calls to `http://<host>/dfmm-api/` and handle them as desired.

#### Model tests (unit tests)

    python DFMM_core/test_all.py

#### API Documentation

[to be added]

#### License

In light of the *grave* threat from possible *leeching* off my *hard* work, I have placed this under the MIT license.  See detailed contents of LICENSE.txt

