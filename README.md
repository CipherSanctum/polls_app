# Django 2.x poll app with F() for speed, and sessions

### PROGRAM CREATED BY:
Kevin from https://CipherSanctum.com

### DESCRIPTION:
This poll app is intended to be plugged into something else, such as a blog_app.

I added the F() class to make database operations much faster by preventing race conditions, and so there is no need to load python values into memory.
That is very useful for databases like sqlite because only 1 write is allowed at a time. And any other database that allows multiple
writes gets improved speed as well.

**The first vote function** uses .latest('pub_date'). It's intended to be used on a home page or some other higher traffic area where
you want a *latest* question to be visible.

**The 2nd function** is useful for any Model, such as a BlogPost, that takes multiple arguments.

Sessions are included to prevent the same person voting more than once.
