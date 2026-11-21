# Query raw SQL

Pass a `sql` operation to `sup.query`. Use a real `baseModelId` on the intended warehouse
connection, and write SQL in that warehouse's dialect. This example uses PostgreSQL table names:

```js
const ordersByStatus = await sup.query({
  baseModelId: '<model id on the orders connection>',
  pipeline: [{
    operation: 'sql',
    parameters: {
      sql: `SELECT status, COUNT(*) AS order_count
            FROM public.orders
            GROUP BY status`,
      fields: [
        { key: 'status', type: 'String' },
        { key: 'order_count', type: 'Number' },
      ],
    },
  }],
  sort: [{ key: 'order_count', direction: 'DESC' }],
  first: 100,
});
// ordersByStatus.rows: [{ status: 'paid', order_count: 42 }, ...]
// Check hasMore; use endCursor as after for the next page.
```

Replace `public.orders` and its columns with actual warehouse names. `fields` keys must match
SQL output column names, including case. The connection defaults to the base model's connection.
The viewer needs **Run SQL Queries** permission. Raw SQL reads warehouse tables directly;
model transformations and model-level row filters are not automatically applied to that SQL.
Use semantic-layer queries or an existing block's output when you need those model rules.

