select *
from vgsales s
where s.publisher = %s and s.genre = %s and s.platform = %s
limit 10