(select 
  l.name,
  cast(l.customers_number as integer) as customers_number
from lawyers l
where l.customers_number = (select max(customers_number) from lawyers))

union all

(select 
  l.name,
  cast(l.customers_number as integer) as customers_number
from lawyers l
where l.customers_number = (select min(customers_number) from lawyers))

union all

select 
  cast('Average' as varchar(100)) as name,
  cast(avg(l.customers_number) as integer) as customers_number
from lawyers l