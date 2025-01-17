INSERT OR IGNORE INTO Area (a_id, a_name) VALUES
(201, '指南路二段大門右半邊附近'),
(202, '噴街（指南路二段119巷）'),
(203, '萬壽路附近');

INSERT OR IGNORE INTO Restaurant (r_id, r_name, a_id) VALUES
('200A', '梁社漢排骨 文山指南店', 201),
('200B', '高句麗', 201),
('200C', '喜記港式燒臘', 201),
('200D', '指南山下海南雞飯', 201),
('200E', '花漾夯夯鍋-政大店', 201),
('200F', '佳味自助餐', 201),
('200G', '提洛斯義式廚房', 201),
('200H', 'Lazy Pasta 慵懶義式廚房文山政大店', 201),
('200I', '栗鍋饗食鍋物文山政大店', 201),
('200J', '滇味廚房', 201),
('200K', '金鮨日式料理', 201),
('200L', '東京小城', 201),
('200M', 'MJ餛飩超人', 201),
('200N', '政大關東煮', 201),
('200O', '隱 Bistro', 201),
('200P', '阿義師海鮮麵', 201),
('200Q', '華越美食', 201),
('200R', 'Purrson Bistro 呼嚕小酒館', 201),
('200S', '驛站熱炒', 201),
('200T', '健康滷味', 201),
('200U', '魯味齋', 201),
('200V', '可麗餅', 202),
('200W', '極鮮滷味', 202),
('200X', '政大排骨王便當', 202),
('200Y', '永康街左撇子', 202),
('200Z', '來來快餐', 202),
('201A', 'Warong Kita 珍妹麵店', 202),
('201B', '原丼力', 202),
('201C', '飽飽食府', 202),
('201D', '悅來牛肉麵', 202),
('201E', '浪速食鋪', 202),
('201F', 'Schumann’s BISTRO NO. 6 舒曼六號餐館 ', 203),
('201G', 'Cow Banana政大店', 203),
('201H', '食鼎鵝肉', 203),
('201I', '小貓咪早餐店', 203),
('201J', '傳香飯糰政大店', 203),
('201K', '古早味蛋餅飯糰', 203),
('201L', '魚樂𩵚魠魚羹', 203),
('201M', 'Juicy Bun Burger 就是棒 美式餐廳 政大店', 203),
('201N', '楊記小吃', 203),
('201O', '口福豆漿店', 203),
('201P', '麥味登 文山政大店', 203),
('201Q', '李白Breakfast x coffee', 203),
('201R', 'Louisa Coffee 路易莎咖啡(政大萬壽門市)', 203),
('201S', 'Spukie 政大店', 203),
('201T', '布朗奇優先早餐店', 201);


INSERT OR IGNORE INTO Type (t_id, t_name) VALUES
(1001, '早餐店'),
(1002, '飲料店'),
(1003, '台式料理'),
(1004, '日式料理'),
(1005, '速食店'),
(1006, '美式料理'),
(1007, '義式料理'),
(1008, '素食料理'),
(1009, '韓式料理'),
(1010, '四川料理'),
(1011, '東南亞料理'),
(1012, '點心類'),
(1013, '餐酒館');

INSERT OR IGNORE INTO Restaurant_Types (r_id, t_id) VALUES
('200A', 1003),
('200B', 1009),
('200C', 1003),
('200D', 1003),
('200E', 1003),
('200F', 1003),
('200G', 1007),
('200H', 1007),
('200I', 1003),
('200J', 1011),
('200K', 1004),
('200L', 1004),
('200M', 1003),
('200N', 1004),
('200O', 1007),
('200O', 1013),
('200P', 1003),
('200Q', 1003),
('200Q', 1011),
('200R', 1007),
('200R', 1013),
('200S', 1003),
('200T', 1003),
('200U', 1003),
('200V', 1012),
('200W', 1003),
('200X', 1003),
('200Y', 1003),
('200Z', 1003),
('201A', 1011),
('201B', 1004),
('201C', 1003),
('201D', 1003),
('201E', 1003),
('201F', 1007),
('201F', 1013),
('201G', 1001),
('201G', 1002),
('201H', 1003),
('201I', 1001),
('201J', 1001),
('201K', 1001),
('201L', 1003),
('201M', 1006),
('201N', 1003),
('201O', 1001),
('201P', 1001),
('201Q', 1001),
('201R', 1002),
('201S', 1005),
('201T', 1001);
