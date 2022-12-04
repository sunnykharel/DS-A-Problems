<h2>  Recyclable and Low Fat Products</h2><hr><div><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Table:</font></font><code>Products</code></p>

<pre><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">+-------------+---------+</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| Column Name | Type    |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
+-------------+---------+</font></font><font></font>
| product_id  | int     |<font></font>
| low_fats    | enum    |<font></font>
| recyclable  | enum    |<font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
+-------------+---------+</font></font><font></font>
product_id is the primary key for this table.<font></font>
low_fats is an ENUM of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.<font></font>
recyclable is an ENUM of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.</pre>

<p>&nbsp;</p>

<p>Write an SQL query to find the ids of products that are both low fat and recyclable.</p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Return the result table in </font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">any order</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">The query result format is in the following example.</font></font></p>

<p>&nbsp;</p>
<p><strong class="example"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Example 1:</font></font></strong></p>

<pre><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Input:</font></font></strong> <font></font>
Products table:<font></font>
+-------------+----------+------------+<font></font>
| product_id  | low_fats | recyclable |<font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
+-------------+----------+------------+</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| </font><font style="vertical-align: inherit;">0 | </font><font style="vertical-align: inherit;">AND | </font><font style="vertical-align: inherit;">No |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| </font><font style="vertical-align: inherit;">1 | </font><font style="vertical-align: inherit;">AND | </font><font style="vertical-align: inherit;">AND |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| </font><font style="vertical-align: inherit;">2 | </font><font style="vertical-align: inherit;">No | </font><font style="vertical-align: inherit;">AND |</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| </font><font style="vertical-align: inherit;">3 | </font><font style="vertical-align: inherit;">AND | </font><font style="vertical-align: inherit;">AND |</font></font><font></font>
| 4           | N        | N          |<font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
+-------------+----------+------------+</font></font><font></font>
<strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Output:</font></font></strong> <font></font>
+-------------+<font></font>
| product_id  |<font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
+-------------+</font></font><font></font>
| 1           |<font></font>
| 3           |<font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
+-------------+</font></font><font></font>
<strong>Explanation:</strong> Only products 1 and 3 are both low fat and recyclable.
</pre>
</div>