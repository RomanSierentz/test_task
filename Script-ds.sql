select count(distinct(seller_id)) from consumption_info;

select avg(fruit_weight), seller_id from seller_info
group by seller_id ; 