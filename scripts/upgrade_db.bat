
            echo "开始迁移数据库..."
            flask db init
            flask db migrate -m 'xxx'
            flask db upgrade
            echo "按任意键继续..."
            pause
            