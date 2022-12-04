<h2>  Big Countries</h2><hr><div><p>Table: <code>World</code></p>

<pre>+-------------+---------+<font></font>
| Column Name | Type    |<font></font>
+-------------+---------+<font></font>
| name        | varchar |<font></font>
| continent   | varchar |<font></font>
| area        | int     |<font></font>
| population  | int     |<font></font>
| gdp         | int     |<font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
+-------------+---------+</font></font><font></font>
name is the primary key column for this table.<font></font>
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.<font></font>
</pre>

<p>&nbsp;</p>

<p>A country is <strong>big</strong> if:</p>

<ul>
	<li>it has an area of at least&nbsp;three million (i.e., <code>3000000 km<sup>2</sup></code>), or</li>
	<li>it has a population of at least&nbsp;twenty-five million (i.e., <code>25000000</code>).</li>
</ul>

<p>Write an SQL query to report the name, population, and area of the <strong>big countries</strong>.</p>

<p>Return the result table in <strong>any order</strong>.</p>

<p>The query result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> <font></font>
World table:<font></font>
+-------------+-----------+---------+------------+--------------+<font></font>
| name        | continent | area    | population | gdp          |<font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
+-------------+-----------+---------+------------+--------------+</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| </font><font style="vertical-align: inherit;">Afghanistan | </font><font style="vertical-align: inherit;">Thing | </font><font style="vertical-align: inherit;">652230 | </font><font style="vertical-align: inherit;">25500100 | </font><font style="vertical-align: inherit;">20343000000 |</font></font><font></font>
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |<font></font>
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |<font></font>
| Andorra     | Europe    | 468     | 78115      | 3712000000   |<font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
| </font><font style="vertical-align: inherit;">Angola | </font><font style="vertical-align: inherit;">Africa | </font><font style="vertical-align: inherit;">1246700 | </font><font style="vertical-align: inherit;">20609294 | </font><font style="vertical-align: inherit;">100990000000 |</font></font><font></font>
+-------------+-----------+---------+------------+--------------+<font></font>
<strong>Output:</strong> <font></font>
+-------------+------------+---------+<font></font>
| name        | population | area    |<font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
+-------------+------------+---------+</font></font><font></font>
| Afghanistan | 25500100   | 652230  |<font></font>
| Algeria     | 37100000   | 2381741 |<font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
+-------------+------------+---------+</font></font><font></font>
</pre>
</div>