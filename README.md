<p align="center"><img width=20% alt="Cool cfcli Logo" src="https://github.com/prasoonbatham11/cfcli/blob/master/images/logo.png"></p>
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
      <li><a href="#compare-two-users">Compare Two Users</a></li>
    </ul>
  </li>
  <li><a href="#todo">TODO</a></li>
  <li><a href="#contribute">Contribute</a></li>
</ul>

## Installation

```bash
pip install cfs
```
<p>OR</p>

```bash
git clone https://github.com/prasoonbatham11/cfcli.git
python3 setup.py install
```

## Usage

<p>Use <strong>-h</strong> or <strong>--help</strong> to see usage.</p>

 ```bash
cfs -h
```

### View User Details

```bash
# Shows basic details of the user specified
cfs -u prasoonbatham
```

![](https://raw.githubusercontent.com/prasoonbatham11/cfcli/master/images/show_user.png)

### View Rating Graph of User

```bash
# Shows Rating change graph of user
cfs -g prasoonbatham
```

<p>Rating Graph of user is displayed as a gnuplot.</p>

![](https://raw.githubusercontent.com/prasoonbatham11/cfcli/master/images/user_graph.png)

### View Contest Details

<p>Contest ID can be found in the url of contest such as: <a href="https://codeforces.com/contest/1137">/contest/<strong>1137</strong>/</a>.</p>

```bash
# Shows details of contest specified by contest id
cfs -c 1137

# To view Contests from gym
cfs -c 102134 --gym
```

![](https://raw.githubusercontent.com/prasoonbatham11/cfcli/master/images/contest.png)

### Interact With Problemset Subcommand Interface

<p>These commands retrieve the specified problemset (by tag or whole) and open a python cmd sub-terminal where various other actions can be performed.</p>

```bash
# Loads all the problems
cfs -p

# Specify a problemset tag
cfs -p --tag dp
```

<p>The sub-interface has the following commands:</p>
<ul>
  <li>View available commands: <strong>?</strong></li>
  <li>List n Problems (max 15): <strong>list n</strong></li>
  <li>Reset the pointer to list problems: <strong>reset</strong></li>
  <li>List problems of contest id 'cid': <strong>listc cid</strong></li>
  <li>List 10 problems specified by index: <strong> listi index</strong></li>
  <li>View problem details specified by name: <strong> listn name</strong></li>
  <li>View problem details specified by index: <strong> prob index</strong></li>
  <li>View problem statement specified by contestid+index: <strong>stat 1133A</strong></li>
</ul>

<p>Say the following is the output for 8 problems</p>

```bash
cf> list 8
0: Circus
1: Sushi for Two
2: Matches Are Not a Child's Play 
3: Train Car Selection
4: Cooperative Game
5: Museums Tour
6: Camp Schedule
7: Skyscrapers
cf> list 8
8: Spanning Tree with One Fixed Degree
9: Spanning Tree with Maximum Degree
10: K Balanced Teams
11: Zero Quantity Maximization
12: Balanced Team
13: Preparation for International Women's Day
14: Middle of the Contest
15: Greedy Subsequences
cf> 
```

<p>To reset the pointer back to 0 we use <strong>reset</strong> command.</p>

<p>Similar to <strong>list</strong>, <strong>listc</strong> is used to list problems of a particular contest.</p>


```bash
cf> listc 1133
8: Spanning Tree with One Fixed Degree
9: Spanning Tree with Maximum Degree
10: K Balanced Teams
11: Zero Quantity Maximization
12: Balanced Team
13: Preparation for International Women's Day
14: Middle of the Contest
```

<p>In codeforces every problem has an index ('A', 'B', etc.). To view the problems by index use <strong>listi</strong>. To reset the pointer, again use <strong>reset</strong> command.</p>

```bash
cf> listi B
0: Circus
6: Camp Schedule
13: Preparation for International Women's Day
20: Discounts
27: Draw!
30: Two Cakes
35: Wrong Answer
39: Mike and Children
45: Once in a casino
53: Tanya and Candies
```

<p><strong>listn</strong> and <strong>prob</strong> are used to view problem details by name and serial number respectively</p>

```bash
cf> listn Sushi for Two
        |Problem Details

        |Name            :    Sushi for Two
        |Contest ID      :    1138      
        |Index           :    A         
        |Points          :    500.0     
        |Rating          :    900       
        |Solved By       :    3940      
cf> prob 0
        |Problem Details

        |Name            :    Circus    
        |Contest ID      :    1138      
        |Index           :    B         
        |Points          :    1000.0    
        |Rating          :    1700      
        |Solved By       :    1147 
```

<p>To view any problem statement use <strong>stat</strong> command. This opens a paged output where you can see problem statement.</p>

```bash
cf> stat 1133A
```

### View A Blog Entry Specified By Blog ID

<p>Blog ID can be found in the url of blog such as: <a href="https://codeforces.com/blog/entry/14565">/blog/entry/<strong>14565</strong>/</a>.</p>

```bash
# View blog specified by blog id
cfs -b 14565
```

<p>The blog is displayed in a paged output with a proper comment thread. The comment thread is hierarchical, i.e., a reply to a comment is separated by one tab space from its parent comment.</p>

![](https://raw.githubusercontent.com/prasoonbatham11/cfcli/master/images/blog.png)

### View Rating Change For Users In A Contest

```bash
# View blog specified by blog id
cfs -rc 1137

# Specify a particular handle
cfs -rc 1137 --handle Petr
```

![](https://raw.githubusercontent.com/prasoonbatham11/cfcli/master/images/rating_change.png)

### Get Blog Entries Of A User

```bash
# Get all blog entries of Petr
cfs -bu Petr
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
cfs -us prasoonbatham
```

<p>You can also specify fr and count arguments to see <strong>count</strong> number of submissions from a particular index <strong>fr</strong>.</p>
 
 ```bash
# Display 10 submissions from 5th index
cfs -us prasoonbatham --fr 5 --count 10
```
 
<p>The default values for <strong>fr</strong> and <strong>count</strong> are 1 and 10 respectively. If either one of these are specified the other one takes default value.</p>

<p>For instance, if we want to retrieve 10 submissions from 5th index we can write.</p>

 ```bash
# Here count takes the default value 10
cfs -us prasoonbatham --fr 5
```

<p>Similarly,</p>

 ```bash
# Display 20 submissions from 1st index
cfs -us prasoonbatham --count 20
```

![](https://raw.githubusercontent.com/prasoonbatham11/cfcli/master/images/submissions_user.png)

### View Contest Submissions

 ```bash
# Display contest submissions specified by contest id
cfs -cs 1137
```

<p>Here too you can specify <strong>fr</strong> and <strong>count</strong> arguments to see submissions. And it works similar to user submissions.</p>

 ```bash
# Display 100 submissions from index 50
cfs -cs 1137 --fr 50 --count 100
```

<p>Another optional parameter to specify here is: <strong>handle</strong> which retrieves submissions only by the user specified.</p>

 ```bash
# Display 10 submissions for user Petr from index 3 in contest 556
cfs -cs 556 --fr 3 --count 10 --handle Petr
```

![](https://raw.githubusercontent.com/prasoonbatham11/cfcli/master/images/submissions_contest.png)

### Compare Two Users

 ```bash
cfs --compare prasoonbatham Petr
```

![](https://raw.githubusercontent.com/prasoonbatham11/cfcli/master/images/compare.png)

<p>Seriously who am I comparing myself to!</p>

## TODO

- [ ] Add Command for submitting a solution.
- [ ] Improve rendering of problem statement.

## Contribute

<ul>
  <li><a href="https://github.com/prasoonbatham11/cfcli/issues">Have an issue?</a></li>
  <li>Feel free to send feedback via <a href="mailto:prasoonbatham@gmail.com">mail</a></li>
</ul>
