# Report for Assignment 1

## Project chosen

Name: Spotify Downloader

URL: [Shttps://github.com/spotDL/spotify-downloader](https://github.com/spotDL/spotify-downloader)

Number of lines of code and the tool used to count it: Lizard counted 95 KLOC

Programming language: Python

## Coverage measurement

### Existing tool

We used Coverage.py for our test and we ran "coverage run pytest", then "coverage report" to get the table bellow.

![alt text](image.png)

### Your own coverage tool

<The following is supposed to be repeated for each group member>

Erik Doytchinov

yt_dlp_progress_hook()

![alt text](erik-img-1.png)

![alt text](erik-img-2.png)

notify_error()

![alt text](erik-img-3.png)

![alt text](erik-img-4.png)

Ongun Manav

get_status()

![alt text](ongun-img5.png)

![alt text](ongun-img8.png)

format()

![alt text](ongun-img6.png)

![alt text](ongun-img7.png)

## Coverage improvement

### Individual tests

Erik Doytchinov

test_yt_dlp_progress_hook()

![alt text](erik-img-5.png)

![alt text](erik-img-6.png)

![alt text](erik-img-7.png)

Added a test scanario that covers the missing branch, in the case that no file byte size is included.

notify_error()

![alt text](erik-img-8.png)

![alt text](erik-img-9.png)

![alt text](erik-img-10.png)

At first there was no test coverage at all but now all branches are covered.

Ongun Manav

get_status()

![alt text](ongun-img9.png)

![alt text](ongun-img1.png)

![alt text](ongun-img2.png)

Initially the nested if branch was not run, now with the added test for status code 403, it is covered, increasing the coverage form %87.1 to %100

format()

![alt text](ongun-img10.png)

![alt text](ongun-img3.png)

![alt text](ongun-img4.png)

Initially no branch was not covered, now with the new parameters added to the map, increasing the coverage form %4.3 to %91.3

### Overall

Old coverage:

![alt text](image.png)

New coverage after modifications:

![alt text](cov-after.png)

## Statement of individual contributions

Ongun Manav: Contributed in the resolution of finding an eligible repo which initially was our biggest issue. Created branch testing for the functions get_status() and format() in the files github.py and logging.py respectively. Enhanced the tests for both functions by creating a new test case for get_status() and expanding the input_output_map in the existing test for format().

Erik Doytchinov: Contributed in finding a eligible repo, setup and forked it, and figured out how dependencies and project structure works. Then created a instrumentation file that provides us with a tool that is expendable and is base template for our coverage needs. yt_dlp_progress_hook(), notify_error() were the two function functions I provided instrumentation and enhanced coverage results.
