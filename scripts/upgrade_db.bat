
            echo "��ʼǨ�����ݿ�..."
            flask db init
            flask db migrate -m 'xxx'
            flask db upgrade
            echo "�����������..."
            pause
            