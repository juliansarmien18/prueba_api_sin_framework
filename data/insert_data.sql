--INSERT INFORMATION FOR BOOKS

INSERT INTO Books(
    name, pages
)
VALUES (
'Book 1',
5
);
INSERT INTO Books(
    name, pages
)
VALUES (
'Book 2',
5
);
INSERT INTO Books(
    name, pages
)
VALUES (
'Book 3',
5
);
INSERT INTO Books(
    name, pages
)
VALUES (
'Book 4',
4
);
INSERT INTO Books(
    name, pages
)
VALUES (
'Book 5',
6
);

--INSET INFORMATION FOR FORMATS
INSERT INTO Formats(
format
)
VALUES(
'html'
);
INSERT INTO Formats(
format
)
VALUES(
'text'
);


--INSERT FOR PAGES

--Book 1
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
1,
'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
1
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
2,
'Nunc ultricies ut justo dapibus tristique',
1
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
3,
'uisque blandit elementum velit nec luctus',
1
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
4,
'Quisque in massa eu tellus elementum tincidunt.',
1
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
5,
'Mauris lacus odio, vestibulum in rutrum id, pellentesque vitae tortor.',
1
);

--Book 2
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
1,
'Integer sodales imperdiet urna, vel cursus nulla finibus et',
2
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
2,
'Quisque id mi rhoncus, mattis sapien feugiat, pellentesque mauris.',
2
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
3,
'Aenean viverra tempor orci, eget fermentum nulla rhoncus sed. ',
2
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
4,
'Donec molestie lorem sit amet tortor condimentum, vitae molestie eros maximus. ',
2
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
5,
'Ut non egestas orci. Suspendisse tincidunt tortor laoreet tempus blandit. ',
2
);

--Boook 3
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
1,
'Donec eu vestibulum enim, in hendrerit tellus. Nulla volutpat blandit commodo',
3
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
2,
'Etiam id orci volutpat, vehicula lacus in, accumsan purus',
3
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
3,
'Duis rhoncus suscipit ex sit amet consequat. Sed at dolor quis sapien accumsan elementum a eu ante.',
3
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
4,
'Etiam porttitor sapien a vestibulum maximus. Nulla mollis velit enim, et feugiat ligula vulputate id.',
3
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
5,
'Suspendisse suscipit lorem sit amet congue efficitur. Curabitur tincidunt gravida volutpat.',
3
);

--Book 4
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
1,
'Mauris placerat tincidunt mi, ut commodo lorem mattis nec',
4
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
2,
'Quisque sit amet nibh tincidunt, imperdiet diam et, efficitur erat.',
4
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
3,
'Vivamus vel odio nisi. Donec commodo purus non tellus mattis iaculis.',
4
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
4,
'Nulla tincidunt odio ut quam efficitur, sed lacinia massa aliquet.',
4
);

--Book 5
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
1,
'Aliquam euismod orci fringilla, sollicitudin purus a, tristique nisl.',
5
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
2,
'Aenean scelerisque a arcu a mollis. Ut ac risus quis magna tempor fermentum.',
5
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
3,
'Duis lacinia velit id tincidunt aliquam. Ut fermentum venenatis justo id lacinia. ',
5
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
4,
'Phasellus sapien nulla, rutrum eu turpis non, placerat imperdiet metus.',
5
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
5,
'Aliquam sollicitudin metus ac lorem gravida consectetur. ',
5
);
INSERT INTO Pages(
page,
content,
book_id
)
VALUES(
6,
'Duis sodales diam eget dolor lobortis lacinia. Donec scelerisque vitae est convallis facilisis. ',
5
);
