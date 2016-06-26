# webapp_kadai

ファイル構造  

/  
	app/  
    controllers/  
      _init_.py  
      mistake.py  
    models/  
      _init_.py  
      db.py  
      mistake.py  
      pager.py  
    _init_.py  
  config/  
    db.cnf  
  libs/  
    bottle.py  
  sql/  
    create_table.sql  
  stat/  
    css/  
      style.css  
  views/  
    inc/  
      header.html  
      footer.html  
    edit.html  
    index.html  
    new.html  
  index.py  
    
  index.py：ディスパッチャー　python index.pyで稼働  
  bottle.py：PythonのWebアプリフレームワークbottleの本体  
  db.cnf, create_table.sql：MySQLの情報  
