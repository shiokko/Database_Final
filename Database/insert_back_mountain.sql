INSERT OR IGNORE INTO Area (a_id, a_name) VALUES
(401, '恆光街附近'),
(402, '木新路二段附近'),
(403, '木新路三段附近'),
(404, '興隆路附近');

INSERT OR IGNORE INTO Restaurant (r_id, r_name, a_id) VALUES
('400A', '五行水餃專賣店', 401),
('400B', '邁可船釣生魚片', 401),
('400C', '恆光街香酥雞', 401),
('400D', '淑姐營養三明治', 401),
('400E', '陽城燒臘', 401),
('400F', 'Q Burger 文山恆光店', 401),
('400G', '萬華莊家班麻油雞 木新店', 402),
('400H', '早。自己//木新店', 402),
('400I', '大隻佬 麵料理', 402),
('400J', 'Lion手工蛋餅', 402),
('400K', '品佳牛肉麵', 402),
('400L', '牛大哥', 402),
('400M', '匠記日式食堂', 402),
('400N', 'Single&Double', 402),
('400O', 'LI RA義大利廚房', 403),
('400P', '錢都日式涮涮鍋-木柵木新店', 403),
('400Q', '木柵老爹鵝肉專賣店', 403),
('400R', '山的另一邊', 403),
('400S', '木柵米粉湯', 403),
('400T', '寶杏堂手切滷肉飯 溫補羊肉湯', 403),
('400U', '開源社雞排 木新店', 403),
('400V', '漢堡王 木新店', 403),
('400W', '三尋九食臭臭鍋 （木柵店）', 403),
('400X', '爭鮮迴轉壽司-木新店', 403),
('400Y', 'Rico義式廚房 文山木新店', 404),
('400Z', '狂魔炒飯x餓鬼糧倉-文山店', 404),
('401A', '思月小館義大利麵', 404),
('401B', '欣欣大眾魷魚羹', 404),
('401C', '咖哩空間-木柵興隆店', 404),
('401D', '麵匡匡拉麵食堂 木柵興隆店', 404),
('401E', '石二鍋 台北興隆店', 404),
('401F', 'MootyDiner 莫蒂早午餐', 404);


INSERT OR IGNORE INTO Type (t_id, t_name) VALUES
(1001, '早餐店'),
(1002, '飲料店'),
(1003, '台式料理'),
(1004, '日式料理'),
(1005, '速食店'),
(1006, '美式料理'),
(1007, '義式料理');

INSERT OR IGNORE INTO Restaurant_Types (r_id, t_id) VALUES
('400A', 1003),
('400B', 1004),
('400C', 1003),
('400D', 1001),
('400E', 1003),
('400F', 1006),
('400G', 1003),
('400H', 1001),
('400I', 1003),
('400J', 1001),
('400K', 1003),
('400L', 1003),
('400M', 1004),
('400N', 1007),
('400O', 1007),
('400P', 1004),
('400Q', 1003),
('400R', 1003),
('400S', 1003),
('400T', 1003),
('400U', 1003),
('400V', 1005),
('400W', 1003),
('400X', 1004),
('400Y', 1007),
('400Z', 1003),
('401A', 1007),
('401B', 1003),
('401C', 1003),
('401D', 1003),
('401E', 1004),
('401F', 1001);





