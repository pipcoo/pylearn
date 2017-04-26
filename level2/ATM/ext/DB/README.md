



create database
#show databases

use emp

create table tab1 (id int ,name str)

{
    "columns": [
        {
            "staff_id": "int"
        },
        {
            "name": "str"
        },
        {
            "age": "int"
        },
        {
            "phone": "str"
        },
        {
            "dept": "str"
        },
        {
            "enroll_date": "str"
        }
    ],
    "table_data": [
        [
            0,
            [
                1,
                "Alex Li4",
                22,
                "13651054608",
                "IT",
                "2013-04-01"
            ]
        ],
        [
            1,
            [
                2,
                "Alex Li5",
                22,
                "13651054608",
                "IT",
                "2013-04-01"
            ]
        ],
        [
            2,
            [
                3,
                "Alex Li6",
                22,
                "13651054608",
                "IT",
                "2013-04-01"
            ]
        ],
        [
            3,
            [
                4,
                "Alex Li7",
                22,
                "13651054608",
                "IT",
                "2013-04-01"
            ]
        ],
        [
            4,
            [
                5,
                "Alex Li8",
                22,
                "13651054608",
                "IT",
                "2013-04-01"
            ]
        ],
        [
            5,
            [
                6,
                "Alex Li9",
                22,
                "13651054608",
                "IT",
                "2013-04-01"
            ]
        ]
    ],
    "not_null_col": [
        "staff_id"
    ],
    "auto_add_col": "staff_id",
    "unique": [],
    "cur_auto_add_num": 0,
    "create_tab_ddl": "create table staff_table (staff_id int not null auto_increment,name str,age int ,phone str ,dept str,enroll_date str )"
}


select * from xxx  where xxx = sss and xx = sss

select in,name from xxx  where

insert into xxx values ()
insert into xxx  () values ()

staff_table
---
| staff_id | name | age |
