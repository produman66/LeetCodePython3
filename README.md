# Соглашение о коммитах для команды разработки

## Общие правила
1. Язык: Все сообщения коммитов должны быть на английском языке
2. Формат: Сообщение коммита должно следовать структуре:
  - Заголовок (обязательно)
  - Описание (рекомендуется для сложных изменений)
  - Описание разбивать на строки выделяя поинты

### Структура заголовка 
```
<type>(<scope>): <subject>
```
#### Типы изменений 
- feat: Добавление нового функционала.
- fix: Исправление ошибки.
- docs: Изменения в документации.
- style: Изменения, не влияющие на логику кода (пробелы, форматирование, точка с запятой и т.д.).
- refactor: Изменения в коде, не исправляющие ошибки и не добавляющие новый функционал.
- perf: Изменения, направленные на улучшение производительности.
- test: Добавление или исправление тестов.
- build: Изменения, влияющие на систему сборки или зависимости внешних инструментов.
- ci: Изменения в настройках CI/CD.
- chore: Прочие изменения, не влияющие на исходный код (обновление зависимостей, изменения в конфигурационных файлах и т.д.).
- revert: Откат к предыдущему коммиту.

### Примеры заголовков 
- feat(authentication): add login functionality
- fix(user-profile): correct user profile image display
- docs(readme): update installation instructions
- style(app): reformat codebase with new linter rules
- refactor(database): optimize query performance
- perf(image-processing): improve image compression algorithm
- test(auth): add unit tests for login service
- build(dependencies): update dependency versions
- ci(github-actions): add deployment workflow
- chore(dependencies): update eslint to latest version
- revert: revert commit abc123

### Формат описания
- Краткое описание: Более детальное объяснение изменений, чем в заголовке.
- Ссылки: Ссылки на задачи или тикеты.

### Примеры описания 
```
feat(authentication): add login functionality

Implemented login functionality using OAuth 2.0. This allows users to log in with their Google account.

- Integrated Google Sign-In API
- Added user session management
- Updated UI to include login button

This change addresses the following issues:
- [YGM-47: [Android] Три состояния шторки](https://tracker.yandex.ru/YGM-47)
```

## Примечание 

- Всегда проверяйте свои коммиты перед их пушем.
- Используйте ветки для работы над новыми фичами, исправлениями ошибок и т.д. Веткам следует давать осмысленные имена, такие как android-feature-map, backend-fix-image-display, и т.д.


   
