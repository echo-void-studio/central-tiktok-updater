# Central TikTok Watch — AyuGram / exteraGram

Экспериментальный Python-плагин, отслеживающий публикации **TikTok Private Plus ARM8** в [@CentralTikTok](https://t.me/CentralTikTok).

**Версия:** 0.1.0, прототип. Работа в реальном AyuGram пока не подтверждена. Плагин отслеживает новые сообщения и может проверять публичную страницу канала. Он **не скачивает и не устанавливает APK**, не проверяет подпись APK и **не сравнивает** её с версией установленного TikTok.

## Добавление репозитория

AyuGram / exteraGram → Настройки → Плагины → Каталог → Репозитории → Добавить Git-репозиторий:

`https://github.com/echo-void-studio/central-tiktok-updater`

Репозиторий должен быть **Public**, иначе каталог не сможет прочитать индекс через HTTPS. Для установки из Git может потребоваться разрешить Unknown sources. Проверь права и код плагина.

Ссылка для добавления (в поддерживаемых клиентах):
`https://t.me/exteraPluginRepo?git=https%3A%2F%2Fgithub.com%2Fecho-void-studio%2Fcentral-tiktok-updater`

После установки открой пост с APK Private Plus ARM8 в @CentralTikTok, удерживай сообщение, выбери «Отслеживать Private Plus ARM8». В настройках плагина есть тест уведомления и ручная проверка.

## Разработка

Главный файл: `plugins/central_tiktok_watch.plugin`. Метаданные `__id__` и `__version__` находятся в начале файла. При обновлениях сохраняй `__id__` и увеличивай `__version__`.

```sh
python build_index.py
python build_index.py --check
```

Скрипт обновляет `extera-plugins.json` (SHA-256 и размер файла). GitHub Actions повторяет это на push в `main`; для автокоммита нужны разрешения **Settings → Actions → General → Workflow permissions → Read and write permissions**.

## Структура

```text
README.md
extera-plugins.json
build_index.py
plugins/central_tiktok_watch.plugin
.github/workflows/index.yml
```

## Безопасность

Плагин сторонний и не связан официально с TikTok, AyuGram или exteraGram. APK из сторонних источников устанавливаются на риск пользователя. Контрольная сумма в индексе подтверждает соответствие **плагина** записи в каталоге, но не безопасность TikTok APK.

Спецификация: https://plugins.exteragram.app/docs/plugin-repositories
