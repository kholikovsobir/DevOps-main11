DECLARE курсор_name CURSOR FOR 
SELECT поле1 FROM ИмяТаблицы;

OPEN курсор_name;
FETCH NEXT FROM курсор_name INTO @переменная;

WHILE @@FETCH_STATUS = 0
BEGIN
    -- Обработка текущей строки
    FETCH NEXT FROM курсор_name INTO @переменная;
END;

CLOSE курсор_name;
DEALLOCATE курсор_name;
