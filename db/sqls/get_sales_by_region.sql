select 'NA' as region, sum(na_sales) as sales from vgsales s
union all
select 'EU' as region, sum(eu_sales) as sales from vgsales s
union all
select 'JP' as region, sum(s.gp_sales) as sales from vgsales s
union all
select 'Global' as region, sum(s.global_sales) as sales from vgsales s