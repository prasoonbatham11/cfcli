<p align="center"><img width=20% src="https://github.com/prasoonbatham11/cfcli/blob/master/images/logo.png"></p>
<h4 align="center">Codeforces cli for lazy nerds who don't want to leave their cozy terminals.</h4>

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)

<ul>
  <li><a href="#installation">Installation</a></li>
  <li>
    <a href="#usage">Usage</a>  
    <ul>
      <li><a href="#view-user-details">View User Details</a></li>
      <li><a href="#view-rating-graph-of-user">View Rating Graph of User</a></li>
      <li><a href="#view-contest-details">View Contest Details</a></li>
      <li><a href="#interact-with-problemset-subcommand-interface">Interact With Problemset Subcommand Interface</a></li>
      <li><a href="#view-a-blog-entry-specified-by-blog-id">View A Blog Entry Specified By Blog ID</a></li>
      <li><a href="#view-rating-change-for-users-in-a-contest">View Rating Change For Users In A Contest</a></li>
      <li><a href="#get-blog-entries-of-a-user">Get Blog Entries Of A User</a></li>
      <li><a href="#get-submissions-for-a-specified-user">Get Submissions For A Specified User</a></li>
      <li><a href="#view-contest-submissions">View Contest Submissions</a></li>
      <li><a href="#compare-2-users">Compare 2 Users</a></li>
    </ul>
  </li>
</ul>

## Installation

```bash
pip install cfcli
```
<p>OR</p>

```bash
git clone https://github.com/prasoonbatham11/cfcli.git
python3 setup.py install
```

## Usage

<p>Use <strong>-h</strong> or <strong>--help</strong> to see usage</p>

 ```bash
cf -h
```

### View User Details

```bash
# Shows basic details of the user specified
cf -u prasoonbatham
```

### View Rating Graph of User

```bash
# Shows Rating change graph of user
cf -g prasoonbatham
```

<p>Rating Graph of user is displayed as a gnuplot</p>

### View Contest Details

<p>Contest ID can be found in the url of contest such as: <a href="https://codeforces.com/contest/1137">/contest/<strong>1137</strong>/</a></p>

```bash
# Shows details of contest specified by contest id
cf -g 1137

# To view Contests from gym
cf -g 1133 --gym
```

### Interact With Problemset Subcommand Interface

```bash
# Loads all the problems
cf -p

# Specify a problemset tag
cf -p --tag dp
```

### View A Blog Entry Specified By Blog ID

<p>Blog ID can be found in the url of blog such as: <a href="https://codeforces.com/blog/entry/14565">/blog/entry/<strong>14565</strong>/</a></p>

```bash
# View blog specified by blog id
cf -b 14565
```

<p>The blog is displayed in a paged output with a proper comment thread. The comment thread is hierarchical, i.e., a reply to a comment is separated by one tab space from its parent comment.</p>

### View Rating Change For Users In A Contest

```bash
# View blog specified by blog id
cf -rc 1137

# Specify a particular handle
cf -rc 1137 --handle Petr
```

### Get Blog Entries Of A User

```bash
# Get all blog entries of Petr
cf -bu Petr
```

<p>The subcommand interface is implemented using cmd python package and has the following commands.</p>
<ul>
  <li>View available commands: <strong>?</strong></li>
  <li>List n Blog Entries (max 15): <strong>list n</strong></li>
  <li>Reset the pointer to list blog entries from: <strong>reset</strong></li>
  <li>View particular blog entry specified by index: <strong>vidx 65854</strong></li>
  <li>View particular blog entry specified by serial no: <strong> viewi 13</strong></li>
</ul>

<p>Say we get the following output by running <strong>list 5</strong> for user Petr:</p>

```bash
cf> list 5
0: 65854   An oracle week
1: 65574   A WTF week
2: 65328   A snack week
3: 65152   A tourist week
4: 64991   A mumbling week
```
<p>Running <strong>list 5</strong> again will return the next 5 entries.Now an internal pointer idx points to entry 10. To reset it we run <strong>reset</strong>.</p>

```bash
cf> list 5
5: 64854   A Galois week
6: 64669   An anti-library week
7: 64501   A Dilworth week
8: 64349   A Radewoosh week
9: 64346   And the best problem of 2018 is...
cf> reset
cf> list 5
0: 65854   An oracle week
1: 65574   A WTF week
2: 65328   A snack week
3: 65152   A tourist week
4: 64991   A mumbling week
cf> 
```
<p>To view the entry <strong>A galois week</strong> we can either run:</p>

```bash
cf> viewi 5 
```

<p>OR</p>

```bash
cf> vidx 64854  
```

### Get Submissions For A Specified User

<p>To display all the submissions of the user use:</p>

```bash
cf -us prasoonbatham
```

<p>You can also specify fr and count arguments to see <strong>count</strong> number of submissions from a particular index <strong>fr</strong></p>
 
 ```bash
# Display 10 submissions from 5th index
cf -us prasoonbatham --fr 5 --count 10
```
 
<p>The default values for <strong>fr</strong> and <strong>count</strong> are 1 and 10 respectively. If either one of these are specified the other one takes default value.</p>

<p>For instance, if we want to retrieve 10 submissions from 5th index we can write.</p>

 ```bash
# Here count takes the default value 10
cf -us prasoonbatham --fr 5
```

<p>Similarly.</p>

 ```bash
# Display 20 submissions from 1st index
cf -us prasoonbatham --count 20
```

### View Contest Submissions

 ```bash
# Display contest submissions specified by contest id
cf -cs 1137
```

<p>Here too you can specify <strong>fr</strong> and <strong>count</strong> arguments to see submissions. And it works similar to user submissions</p>

 ```bash
# Display 100 submissions from index 50
cf -cs 1137 --fr 50 --count 100
```

<p>Another optional parameter to specify here is: <strong>handle</strong> which retrieves submissions only by the user specified</p>

 ```bash
# Display 10 submissions for user Petr from index 3 in contest 556
cf -cs 556 --fr 3 --count 10 --handle Petr
```

### Compare 2 Users

 ```bash
cf --compare prasoonbatham Petr
```


