# Program performance with large database

Using the file seed.py found in this directory, the program's performance was tested with and without an index in the program's database. The database thus contained no images, so performance related to images is not observed in this test.

## Without index

Here are the results from testing the program without an index:

```
elapsed time: 0.1 s
127.0.0.1 - - [03/May/2026 15:47:24] "GET / HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:47:24] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.1 s
127.0.0.1 - - [03/May/2026 15:47:27] "GET /2 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:47:27] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.1 s
127.0.0.1 - - [03/May/2026 15:47:28] "GET /3 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:47:28] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.1 s
127.0.0.1 - - [03/May/2026 15:47:30] "GET /4 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:47:30] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.1 s
127.0.0.1 - - [03/May/2026 15:47:32] "GET /5 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:47:32] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.34 s
127.0.0.1 - - [03/May/2026 15:48:05] "GET /find_entry HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:48:05] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.34 s
127.0.0.1 - - [03/May/2026 15:48:08] "GET /find_entry?query=123&order=0 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:48:08] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 1.27 s
127.0.0.1 - - [03/May/2026 15:48:15] "GET /user/123 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:48:15] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.49 s
127.0.0.1 - - [03/May/2026 15:48:22] "GET /user/123/2 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:48:22] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.42 s
127.0.0.1 - - [03/May/2026 15:48:24] "GET /user/123/3 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:48:24] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.42 s
127.0.0.1 - - [03/May/2026 15:48:26] "GET /user/123/4 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:48:26] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.42 s
127.0.0.1 - - [03/May/2026 15:48:28] "GET /user/123/5 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:48:28] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.42 s
127.0.0.1 - - [03/May/2026 15:48:30] "GET /user/123/6 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:48:30] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 1.42 s
127.0.0.1 - - [03/May/2026 15:48:35] "GET /discussions/123 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:48:35] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 1.42 s
127.0.0.1 - - [03/May/2026 15:48:41] "GET /discussions/123/2 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:48:41] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 1.43 s
127.0.0.1 - - [03/May/2026 15:48:47] "GET /discussions/123/3 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:48:47] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 1.63 s
127.0.0.1 - - [03/May/2026 15:49:00] "GET /discussions/123/4 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:49:00] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 1.42 s
127.0.0.1 - - [03/May/2026 15:49:03] "GET /discussions/123/5 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:49:03] "GET /static/main.css HTTP/1.1" 304 -
None
elapsed time: 0.89 s
127.0.0.1 - - [03/May/2026 15:50:04] "GET /entry/338696 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:50:04] "GET /static/main.css HTTP/1.1" 304 -
None
elapsed time: 0.75 s
127.0.0.1 - - [03/May/2026 15:50:10] "GET /entry/338696?order=None&page=2 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 15:50:10] "GET /static/main.css HTTP/1.1" 304 -
```

While the front page is quick and search is reasonably responsive, user pages on both the entry and discussion side are noticeably slower.

## With index

Adding the index:

```
CREATE INDEX idx_entry_user ON Entries (user_id);
CREATE INDEX idx_message_user ON Messages (user_id);
```

we get the following results:

```
elapsed time: 0.27 s
127.0.0.1 - - [03/May/2026 17:50:30] "GET / HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:50:30] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.06 s
127.0.0.1 - - [03/May/2026 17:50:32] "GET /2 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:50:32] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.06 s
127.0.0.1 - - [03/May/2026 17:50:33] "GET /3 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:50:33] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.06 s
127.0.0.1 - - [03/May/2026 17:50:34] "GET /4 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:50:34] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.08 s
127.0.0.1 - - [03/May/2026 17:50:35] "GET /5 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:50:36] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.4 s
127.0.0.1 - - [03/May/2026 17:50:38] "GET /find_entry HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:50:38] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.34 s
127.0.0.1 - - [03/May/2026 17:50:43] "GET /find_entry?query=888&order=0 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:50:43] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.33 s
127.0.0.1 - - [03/May/2026 17:50:46] "GET /find_entry?query=888&order=0&page=2 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:50:46] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.33 s
127.0.0.1 - - [03/May/2026 17:50:47] "GET /find_entry?query=888&order=0&page=3 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:50:47] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.33 s
127.0.0.1 - - [03/May/2026 17:50:49] "GET /find_entry?query=888&order=0&page=4 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:50:49] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.33 s
127.0.0.1 - - [03/May/2026 17:50:50] "GET /find_entry?query=888&order=0&page=5 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:50:50] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 1.26 s
127.0.0.1 - - [03/May/2026 17:50:58] "GET /user/595 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:50:58] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 1.26 s
127.0.0.1 - - [03/May/2026 17:51:01] "GET /user/595/2 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:51:01] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.88 s
127.0.0.1 - - [03/May/2026 17:51:03] "GET /user/595/3 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:51:03] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.38 s
127.0.0.1 - - [03/May/2026 17:51:05] "GET /user/595/4 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:51:05] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.06 s
127.0.0.1 - - [03/May/2026 17:51:07] "GET /user/595/5 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:51:07] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 1.17 s
127.0.0.1 - - [03/May/2026 17:51:22] "GET /discussions/595 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:51:22] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.1 s
127.0.0.1 - - [03/May/2026 17:51:24] "GET /discussions/595/2 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:51:24] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.11 s
127.0.0.1 - - [03/May/2026 17:51:26] "GET /discussions/595/3 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:51:26] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.11 s
127.0.0.1 - - [03/May/2026 17:51:27] "GET /discussions/595/4 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:51:27] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 1.16 s
127.0.0.1 - - [03/May/2026 17:51:29] "GET /discussions/595/5 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:51:29] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.25 s
127.0.0.1 - - [03/May/2026 17:52:41] "GET / HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:52:41] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 1.4 s
127.0.0.1 - - [03/May/2026 17:52:45] "GET /user/220 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:52:45] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 1.38 s
127.0.0.1 - - [03/May/2026 17:52:48] "GET /user/220/2 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:52:48] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 1.38 s
127.0.0.1 - - [03/May/2026 17:52:51] "GET /user/220/3 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:52:51] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 1.39 s
127.0.0.1 - - [03/May/2026 17:52:54] "GET /user/220/4 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:52:54] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 1.38 s
127.0.0.1 - - [03/May/2026 17:52:57] "GET /user/220/5 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:52:57] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 2.76 s
127.0.0.1 - - [03/May/2026 17:53:01] "GET /discussions/220 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:53:01] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 2.75 s
127.0.0.1 - - [03/May/2026 17:53:05] "GET /discussions/220/2 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:53:05] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 2.71 s
127.0.0.1 - - [03/May/2026 17:53:09] "GET /discussions/220/3 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:53:09] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 2.76 s
127.0.0.1 - - [03/May/2026 17:53:13] "GET /discussions/220/4 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:53:13] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 2.77 s
127.0.0.1 - - [03/May/2026 17:53:18] "GET /discussions/220/5 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:53:18] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.02 s
127.0.0.1 - - [03/May/2026 18:08:35] "GET /entry/995509 HTTP/1.1" 200 -
elapsed time: 0.01 s
127.0.0.1 - - [03/May/2026 18:08:35] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 18:08:38] "GET /entry/995509?order=None&page=2 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 18:08:38] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.01 s
127.0.0.1 - - [03/May/2026 18:09:05] "GET /entry/276436 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 18:09:05] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.01 s
127.0.0.1 - - [03/May/2026 18:09:13] "GET /entry/652723 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 18:09:13] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.01 s
127.0.0.1 - - [03/May/2026 18:09:19] "GET /entry/652723?order=0 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 18:09:19] "GET /static/main.css HTTP/1.1" 304 -
```

The results on user pages are very varied. On this test the first user's pages turned out to be much faster than the average test, where the load times were usually around 1.4-1.5 seconds like on the non-index tests, so I decided to test on another user in the same test. On the first user page, the results are returned many times faster than on the second. I have no idea why and not enough time, patience and/or knowhow how to find out. 

Despite the confusing results on user pages, the site is slightly faster on other pages. The biggest improvement is found on entry pages.

## Conclusions

The results indicate that even while utilising indexes, this version of the program has its limitations with large quantities of data. The current implementation is more fit for smaller enthusiast communities than large general audiences if the performance of the site is to be kept at good levels. Databases work in mysterious ways.