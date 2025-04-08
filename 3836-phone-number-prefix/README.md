<h2><a href="https://leetcode.com/problems/phone-number-prefix">3836. Phone Number Prefix</a></h2><h3>Easy</h3><hr><p>You are given a string array <code>numbers</code> that represents phone numbers. Return <code>true</code> if no phone number is a prefix of any other phone number; otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">numbers = [&quot;1&quot;,&quot;2&quot;,&quot;4&quot;,&quot;3&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>No number is a prefix of another number, so the output is <code>true</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">numbers = [&quot;001&quot;,&quot;007&quot;,&quot;15&quot;,&quot;00153&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>The string <code>&quot;001&quot;</code> is a prefix of the string <code>&quot;00153&quot;</code>. Thus, the output is <code>false</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= numbers.length &lt;= 50</code></li>
	<li><code>1 &lt;= numbers[i].length &lt;= 50</code></li>
	<li>All numbers contain only digits <code>&#39;0&#39;</code> to <code>&#39;9&#39;</code>.</li>
</ul>
