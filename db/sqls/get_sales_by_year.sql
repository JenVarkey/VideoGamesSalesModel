select s.year,sum(s.global_sales)as sales
from vgsales s
where s.year is not null
group by s.year
order by s.year
limit 5