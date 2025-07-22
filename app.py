from flask import Flask, render_template_string, request  # Добавили request в импорт
import random

app = Flask(__name__)

error_messages = [
    'Уверен?',
    'Точно?',
    'Это путь?',
    'Не промахнулся?',
    'Куда идём?',
    'Снова проверить?',
    'Навигатор сбился?',
    'Не туда свернули?',
    'Такой папки нет… ещё раз?',
    'Может, вернёмся?',
    'Попробовать снова?'
]

error_files = [
    'Упс, ошибка!',
    'А вот и нет',
    'Не угадал!',
    'Мимо кассы.',
    'Пусто‑пусто!',
    'Сюда нельзя.',
    'Хм… здесь ничего.',
    'Тут лишь эхо.',
    'Следы обрываются…',
    'Попробуй ещё раз.',
    'Ай-ай‑ай, ошибочка!',
    'Дверь закрыта.'
]

folder_structure = {
    'Новая папка':{
        'Разделы вопросов':{
            'Криптография': {
                'Какой алгоритм асимметричный': {
                    'AES': {random.choice(error_messages):{}},
                    'RSA': {
                        'Что длиннее в RSA': {
                            'Публичный ключ': {random.choice(error_messages):{}},
                            'Приватный ключ': {
                                'Хэши': {
                                    'Устойчив ли SHA-1 к коллизиям': {
                                        'Да': {random.choice(error_messages):{}},
                                        'Нет': {
                                            'Сети и Протоколы': {
                                                'TCP IP': {
                                                    'Порт DNS': {
                                                        '53': {
                                                            'Безопасные протоколы': {
                                                                'Какой протокол использует порт 22': {
                                                                    'Telnet': {random.choice(error_messages):{}},
                                                                    'SSH': {
                                                                        'VPN': {
                                                                            'Тип VPN с наименьшей задержкой': {
                                                                                'IPSec': {random.choice(error_messages):{}},
                                                                                'WireGuard': {
                                                                                    'Угрозы': {
                                                                                        'Атака на DNS': {
                                                                                            'ARP Spoofing': {random.choice(error_messages):{}},
                                                                                            'DNS Cache Poisoning': {
                                                                                                'Веб безопасность': {
                                                                                                    'Инъекции': {
                                                                                                        'Как защититься от SQLi': {
                                                                                                            'Экранирование': {random.choice(error_messages):{}},
                                                                                                            'Prepared Statements': {
                                                                                                                'XSS': {
                                                                                                                    'Тип XSS на стороне сервера': {
                                                                                                                        'Stored': {
                                                                                                                            'CSRF': {
                                                                                                                                'Защита от CSRF': {
                                                                                                                                    'CAPTCHA': {random.choice(error_messages):{}},
                                                                                                                                    'Anti-CSRF Tokens': {
                                                                                                                                        'Операционные системы': {
                                                                                                                                            'Linux': {
                                                                                                                                                'Разрешения': {
                                                                                                                                                    'Права для ssh private key': {
                                                                                                                                                        '777': {random.choice(error_messages):{}},
                                                                                                                                                        '644': {random.choice(error_messages):{}},
                                                                                                                                                        '600': {
                                                                                                                                                            'SELinux': {
                                                                                                                                                                'Режим по умолчанию': {
                                                                                                                                                                    'Permissive': {random.choice(error_messages):{}},
                                                                                                                                                                    'Enforcing': {
                                                                                                                                                                        'Windows': {
                                                                                                                                                                            'ActiveDirectory': {
                                                                                                                                                                                'Протокол аутентификации': {
                                                                                                                                                                                    'LDAP': {random.choice(error_messages):{}},
                                                                                                                                                                                    'Kerberos': {
                                                                                                                                                                                        'Forensics': {
                                                                                                                                                                                            'Где искать артефакты': {
                                                                                                                                                                                                '$MFT': {
                                                                                                                                                                                                    'Память': {
                                                                                                                                                                                                        'Формат дампа': {
                                                                                                                                                                                                            'RAW': {
                                                                                                                                                                                                                'Киберкриминалистика': {
                                                                                                                                                                                                                    'Первое действие при инциденте': {
                                                                                                                                                                                                                        'Отключить сеть': {random.choice(error_messages):{}},
                                                                                                                                                                                                                        'Сделать образ памяти': {
                                                                                                                                                                                                                            'Жесткий диск': {
                                                                                                                                                                                                                                'Тип образа': {
                                                                                                                                                                                                                                    'RAW': {
                                                                                                                                                                                                                                        'Анализ': {
                                                                                                                                                                                                                                            'Где искать удаленные файлы': {
                                                                                                                                                                                                                                                '$Recycle.Bin': {
                                                                                                                                                                                                                                                    'Таймлайн': {
                                                                                                                                                                                                                                                        'Ключевой атрибут MFT': {
                                                                                                                                                                                                                                                            '$STANDARD_INFORMATION': {
                                                                                                                                                                                                                                                                'Безопасность данных': {
                                                                                                                                                                                                                                                                    'Шифрование': {
                                                                                                                                                                                                                                                                        'Лучший метод для дисков': {
                                                                                                                                                                                                                                                                            'AES-128': {random.choice(error_messages):{}},
                                                                                                                                                                                                                                                                            'AES-256-XTS': {
                                                                                                                                                                                                                                                                                'Резервное копирование': {
                                                                                                                                                                                                                                                                                    'Правило 3-2-1': {
                                                                                                                                                                                                                                                                                        '3 копии на 1 носителе': {random.choice(error_messages):{}},
                                                                                                                                                                                                                                                                                        '3 копии на 2 типах носителей 1 вне сайта': {
                                                                                                                                                                                                                                                                                            'Уничтожение': {
                                                                                                                                                                                                                                                                                                'Метод для SSD': {
                                                                                                                                                                                                                                                                                                    'Форматирование': {random.choice(error_messages):{}},
                                                                                                                                                                                                                                                                                                    'Физическое уничтожение': {
                                                                                                                                                                                                                                                                                                        'DevSecOps': {
                                                                                                                                                                                                                                                                                                            'CI CD': {
                                                                                                                                                                                                                                                                                                                'Безопасность в pipeline': {
                                                                                                                                                                                                                                                                                                                    'SAST': {
                                                                                                                                                                                                                                                                                                                        'Контейнеры': {
                                                                                                                                                                                                                                                                                                                            'Лучшая практика': {
                                                                                                                                                                                                                                                                                                                                'Запуск под root': {random.choice(error_messages):{}},
                                                                                                                                                                                                                                                                                                                                'Read-only файловая система': {
                                                                                                                                                                                                                                                                                                                                    'Kubernetes': {
                                                                                                                                                                                                                                                                                                                                        'Защита Pod': {
                                                                                                                                                                                                                                                                                                                                            'NetworkPolicy': {
                                                                                                                                                                                                                                                                                                                                                'Финальная проверка': {
                                                                                                                                                                                                                                                                                                                                                    'Выберите год первой уязвимости Heartbleed': {
                                                                                                                                                                                                                                                                                                                                                        '2012': {random.choice(error_messages):{}},
                                                                                                                                                                                                                                                                                                                                                        '2014': {
                                                                                                                                                                                                                                                                                                                                                            'flag_storage': {
                                                                                                                                                                                                                                                                                                                                                                'флаг.txt': {
                                                                                                                                                                                                                                                                                                                                                                    'content': 'Кодовое слово: инсайт'}
                                                                                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                                                                                        },
                                                                                                                                                                                                                                                                                                                                                        '2016': {random.choice(error_messages):{}}
                                                                                                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                                                                                                },
                                                                                                                                                                                                                                                                                                                                            },
                                                                                                                                                                                                                                                                                                                                            'LimitRange': {random.choice(error_messages):{}},
                                                                                                                                                                                                                                                                                                                                            'HorizontalPodAutoscaler': {random.choice(error_messages):{}}
                                                                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                                                                                },
                                                                                                                                                                                                                                                                                                                                'Использовать latest тег': {random.choice(error_messages):{}}
                                                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                                                    },
                                                                                                                                                                                                                                                                                                                    'Пентест перед релизом': {random.choice(error_messages):{}},
                                                                                                                                                                                                                                                                                                                    'Ручной код-ревью': {random.choice(error_messages):{}}
                                                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                                        },
                                                                                                                                                                                                                                                                                                    },
                                                                                                                                                                                                                                                                                                    'Шифрование с удалением ключа': {random.choice(error_messages):{}}
                                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                        },
                                                                                                                                                                                                                                                                                        'Ежедневные бэкапы': {random.choice(error_messages):{}}
                                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                            },
                                                                                                                                                                                                                                                                            'Blowfish': {random.choice(error_messages):{}}
                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                },
                                                                                                                                                                                                                                                            },
                                                                                                                                                                                                                                                            '$FILE_NAME': {random.choice(error_messages):{}}
                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                },
                                                                                                                                                                                                                                                '/root': {random.choice(error_messages):{}}
                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                    },
                                                                                                                                                                                                                                    'VMDK': {random.choice(error_messages):{}}
                                                                                                                                                                                                                                }
                                                                                                                                                                                                                            }
                                                                                                                                                                                                                        },
                                                                                                                                                                                                                        'Перезагрузить': {random.choice(error_messages):{}}
                                                                                                                                                                                                                    }
                                                                                                                                                                                                                },
                                                                                                                                                                                                            },
                                                                                                                                                                                                            'JSON': {random.choice(error_messages):{}}
                                                                                                                                                                                                        }
                                                                                                                                                                                                    }
                                                                                                                                                                                                },
                                                                                                                                                                                                'swapfile.sys': {random.choice(error_messages):{}},
                                                                                                                                                                                                '/tmp': {random.choice(error_messages):{}}
                                                                                                                                                                                            }
                                                                                                                                                                                        }
                                                                                                                                                                                    },
                                                                                                                                                                                    'NTLM': {random.choice(error_messages):{}}
                                                                                                                                                                                }
                                                                                                                                                                            }
                                                                                                                                                                        }
                                                                                                                                                                    }
                                                                                                                                                                }
                                                                                                                                                            }
                                                                                                                                                        }
                                                                                                                                                    }
                                                                                                                                                }
                                                                                                                                            }
                                                                                                                                        },
                                                                                                                                    },
                                                                                                                                    'HTTPS': {random.choice(error_messages):{}}
                                                                                                                                }
                                                                                                                            }
                                                                                                                        },
                                                                                                                        'Reflected': {random.choice(error_messages):{}},
                                                                                                                        'DOM-based': {random.choice(error_messages):{}}
                                                                                                                    }
                                                                                                                }
                                                                                                            },
                                                                                                            'WAF': {random.choice(error_messages):{}}
                                                                                                        }
                                                                                                    }
                                                                                                },
                                                                                            },
                                                                                            'SYN Flood': {random.choice(error_messages):{}}
                                                                                        }
                                                                                    }
                                                                                },
                                                                                'OpenVPN': {random.choice(error_messages):{}}
                                                                            }
                                                                        }
                                                                    },
                                                                    'HTTP': {random.choice(error_messages):{}},
                                                                    'RDP': {random.choice(error_messages):{}}
                                                                }
                                                            }
                                                        },
                                                        '67': {random.choice(error_messages):{}},
                                                        '80': {random.choice(error_messages):{}},
                                                        '443': {random.choice(error_messages):{}}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    'ChaCha20': {random.choice(error_messages):{}},
                    'Twofish': {random.choice(error_messages):{}}
                }
            }
        }
    }
}
def get_current_folder(path):
    if not path:
        return folder_structure

    parts = [p for p in path.split('/') if p]
    current = folder_structure

    for part in parts:
        if part in current:
            current = current[part]
        else:
            return None
    return current


@app.route('/')
@app.route('/<path:subpath>')
def show_folder(subpath=''):
    current_folder = get_current_folder(subpath)

    if current_folder is None:
        # Случайное предупреждение
        message = random.choice(error_files)

        # --- вычисляем родительский путь ---
        parts = [p for p in subpath.split('/') if p]  # ['1', '3', '99']
        parent_path = '/'.join(parts[:-1]) if parts else ''  # '1/3'  или ''

        # --- возвращаем HTML с кнопкой "Назад" ---
        return render_template_string('''
            <!DOCTYPE html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Папка не найдена</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 10vw; text-align: center; }
                    h2  { margin-bottom: 25px; }
                    a   { display: inline-block; padding: 10px 16px;
                          background: #f0f0f0; border-radius: 6px;
                          color: #0066cc; text-decoration: none; }
                    a:hover { background: #e0e0e0; }
                </style>
            </head>
            <body>
                <h2>{{ message }}</h2>

                {% if parent_path %}
                    <a href="/{{ parent_path }}">&#8592; Назад</a>
                {% else %}
                    <a href="/">&#8592; На главную</a>
                {% endif %}
            </body>
            </html>
        ''', message=message, parent_path=parent_path)

    if 'content' in current_folder:
        message = 'Кодовое слово: инсайт'
        return render_template_string('''
            <!DOCTYPE html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Папка не найдена</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 10vw; text-align: center; }
                    h2  { margin-bottom: 25px; }
                    a   { display: inline-block; padding: 10px 16px;
                          background: #f0f0f0; border-radius: 6px;
                          color: #0066cc; text-decoration: none; }
                    a:hover { background: #e0e0e0; }
                </style>
            </head>
            <body>
                <h2>{{ message }}</h2>
                <a href="/">&#8592; На главную</a>
            </body>
            </html>
        ''', message=message)

    subfolders = [name for name in current_folder.keys() if name != 'content']
    base_path = subpath + '/' if subpath else ''

    # Вычисляем родительский путь
    parts = [p for p in subpath.split('/') if p]
    parent_path = '/'.join(parts[:-1]) if parts else ''

    # Генерация хлебных крошек
    breadcrumbs = []
    total = len(parts)

    if total > 5:  # путь длиннее 5 папок
        start = total - 5  # индекс первой из последних пяти
        breadcrumbs.append((None, '...'))  # добавляем «…»
    else:
        start = 0  # показываем всё, если ≤5

    # добавляем нужные сегменты (до 5 последних)
    for i in range(start, total):
        path = '/'.join(parts[:i + 1])  # полный путь до текущего сегмента
        breadcrumbs.append((path, parts[i]))

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Поиск задания</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 5vw;
                    font-size: 1rem;
                    line-height: 1.5;
                }

                .breadcrumbs {
                    margin-bottom: 20px;
                    font-size: 0.95rem;
                    word-wrap: break-word;
                }

                .breadcrumbs a {
                    display: inline-block;
                    padding: 10px 15px;
                    background: #f0f0f0;
                    border-radius: 10px;
                    text-decoration: none;
                    color: #333;
                }

                .folder-list {
                    list-style-type: none;
                    padding: 0;
                }

                .folder-list li {
                    margin: 10px 0;
                }

                .folder-list a {
                    display: inline-block;
                    padding: 10px 15px;
                    background: #f0f0f0;
                    border-radius: 10px;
                    text-decoration: none;
                    color: #0066cc;
                    font-size: 1rem;
                }

                .folder-list a:hover {
                    background: #e0e0e0;
                }

                .back-link {
                    margin-bottom: 15px;
                    font-size: 0.95rem;
                    display: inline-block;
                }

                .back-link a {
                    display: inline-block;
                    padding: 10px 15px;
                    background: #f0f0f0;
                    border-radius: 10px;
                    text-decoration: none;
                    color: #333;
                }

                /* 📱 Медиазапрос для маленьких экранов */
                @media (max-width: 600px) {
                    body {
                        margin: 4vw;
                        font-size: 0.95rem;
                    }

                    .folder-list a {
                        padding: 8px 12px;
                        font-size: 0.95rem;
                    }

                    .breadcrumbs {
                        font-size: 0.85rem;
                    }
                }
            </style>
        </head>
        <body>
            <div class="breadcrumbs">
                <a href="/">Главная</a>
                {% for path, name in breadcrumbs %}
                    &raquo; <a href="/{{ path }}">{{ name }}</a>
                {% endfor %}
            </div>

            {% if parent_path %}
                <div class="back-link">
                    <a href="/{{ parent_path }}">&#8592; Назад</a>
                </div>
            {% endif %}

            <h2>Содержимое папки</h2>
            <ul class="folder-list">
                {% for folder in subfolders %}
                    <li><a href="/{{ base_path }}{{ folder }}">{{ folder }}</a></li>
                {% endfor %}
            </ul>
        </body>
        </html>

    ''', subfolders=subfolders, base_path=base_path, subpath=subpath,
                                  parent_path=parent_path, breadcrumbs=breadcrumbs)


if __name__ == '__main__':
    app.run(debug=True)