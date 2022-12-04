<h2>  Find Customer Referee</h2><hr><div><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Table:</font></font><code>Customer</code></p>

<pre><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">+-------------+---------+</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| Column Name | Type    |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
+-------------+---------+</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| id          | int     |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| name        | varchar |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| referee_id  | int     |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
+-------------+---------+</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
id is the primary key column for this table.</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.</font></font><font></font>
</pre>

<p>&nbsp;</p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Write an SQL query to report the names of the customer that are </font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">not referred by</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> the customer with </font></font><code>id = 2</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Return the result table in </font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">any order</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">The query result format is in the following example.</font></font></p>

<p>&nbsp;</p>
<p><strong class="example"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Example 1:</font></font></strong></p>

<pre><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Input:</font></font></strong> <font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
Customer table:</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
+----+------+------------+</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| id | name | referee_id |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
+----+------+------------+</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| 1  | Will | null       |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| 2  | Jane | null       |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| 3  | Alex | 2          |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| 4  | Bill | null       |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| 5  | Zack | 1          |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| 6  | Mark | 2          |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
+----+------+------------+</font></font><font></font>
<strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Output:</font></font></strong> <font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
+------+</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| name |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
+------+</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| Will |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| Jane |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| Bill |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| Zack |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
+------+</font></font><font></font>
</pre>
</div>