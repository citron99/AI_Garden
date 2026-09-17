# AI Garden — состояние реализации

Дата аудита: 2026-08-31.

## Реализовано и проверено автоматически

| Область | Состояние | Проверка |
|---|---|---|
| Валидация JPEG/PNG/WebP, защита от пустых файлов и decompression bomb, повторное кодирование без EXIF/GPS | готово | API- и image-тесты |
| Сады и растения: создание, просмотр, изменение, удаление, изоляция владельцев | готово | API-тесты |
| Реальный мультимодальный OpenAI provider, строгий JSON, безопасный отказ, модель/prompt version, mock-маркировка | готово | provider-тесты с эмуляцией Responses API |
| Вопросы, ответы, повторный анализ, версии, feedback с одним отзывом пользователя | готово | workflow-тесты |
| История растения, включая ответы и версии | готово | API-тесты |
| Приватное получение фотографий без раскрытия пути | готово | ownership-тесты |
| Журнал ухода, напоминания, сезонный календарь | готово | API-тесты |
| Open-Meteo и погодные предупреждения | готово | HTTP mock/cache/error-тесты |
| Web- и Telegram-уведомления с дедупликацией и Celery Beat | готово | notification-тесты |
| Управляемый RAG, OpenAI embeddings, PostgreSQL pgvector/HNSW, срок пересмотра и роли проверки источников | готово как инфраструктура | semantic retrieval, expiry/cache, admin и migration-тесты |
| Пользовательский web UI, privacy, пользовательские и B2B terms на RU/LV/EN | готово | статические, синтаксические и API-тесты |
| Полнота RU/LV/EN, Chromium E2E и axe accessibility gate | готово | 2/2 desktop + Pixel 5: фото → диагноз → ответы → история → feedback → товар → reminder |
| Telegram: одноразовая привязка, команды, подпись webhook, идемпотентность | готово | webhook-тесты |
| Административная панель | готово | RBAC и safe-output тесты |
| Каталог, партнёрский кабинет, роли, атрибуция конверсий, тарифы, счета и обезличенная аналитика | готово | catalog/partner/B2B тесты |
| B2B PDF-счета: снимки реквизитов и строк, стабильный номер, SHA-256, отдельный неизменяемый документ аннулирования с обязательной причиной, защищённая выдача, SMTP-отправка, идемпотентная сверка и аудируемое ручное разрешение несовпадений | готово как операционный контур | API, UI, ownership, tamper, cancellation, delivery, reconciliation и migration-тесты |
| Stripe Checkout/Portal/webhook, подписка и Pro-квоты | готово | signature/idempotency/quota тесты |
| Docker: non-root, healthcheck, `.dockerignore`, PostgreSQL, Redis, worker, beat | готово статически | compose/Dockerfile-тесты |
| Docker image включает `web`, CI собирает образ и выполняет smoke `/health` | готово в коде/CI | локально Docker недоступен |
| `input_status` отделён от `analysis_outcome`; здоровый результат не требует причин | готово | schema/provider-тесты |
| Товарные правила по культуре, проблеме, действию, региону, регистрации и экспертной проверке; moderation workflow | готово | catalog/partner-тесты |
| Версионируемый импорт снимков реестра регулируемых товаров, контрольные суммы и автоматическое отключение отозванных/истёкших правил | готово | registry/API/migration-тесты |
| Атомарный lease/execution token и единая очередь для create/answers/reanalyze | готово | конкурентный worker-тест |
| Восстановление jobs после истечения lease/потери worker, повторная публикация и лимит попыток | готово | maintenance/task queue и PostgreSQL CI-тесты |
| Детерминированный safety gate: дозировки, смешивание, химические действия, безопасная замена и аудит корректировок | готово | policy и end-to-end job-тесты |
| Подтверждение email, reset пароля, HttpOnly refresh cookie, rotation/revoke/reuse detection, rate limit и блокировка | готово | auth/API-тесты |
| Двухфазное удаление платного аккаунта: блокировка → Stripe cancel → webhook → удаление | готово | billing/webhook-тесты |
| GDPR export/delete, S3 private storage, deletion outbox/retry и автоматические сроки очистки | готово как техническая основа | API/storage/maintenance-тесты |
| Повторяемая local→S3 миграция: dry-run, SHA-256/size verification, журнал и `ready_to_switch` | готово | storage migration-тесты |
| PostgreSQL backup/restore CLI с атомарным dump, SHA-256-манифестом и подтверждением цели; S3 versioning/encryption/public-access/lifecycle audit | готово как операторская основа | 6 unit/static-тестов без доступа к production-данным |
| Web refresh после 401 и серверный logout; повторения напоминаний с timezone/DST, snooze и skip | готово | API/i18n и синтаксические тесты |
| Подписанный обезличенный click ID, redirect, idempotency и защищённый partner postback | готово | B2B attribution-тесты |
| Нормализованные taxon/problem/country codes и управляемые локализованные синонимы | готово | recommendation, admin API и migration-тесты |
| Товары: SKU, цена/валюта, наличие, HTTPS-изображение и атомарный CSV-импорт | готово | partner/catalog/API/migration-тесты |
| Upload rate/storage quota, удаление отдельного фото, очистка непривязанных фото и бюджет с failed AI jobs | готово | API/maintenance-тесты |
| Liveness/readiness с БД, миграциями, Redis и worker | готово | API и статические тесты |
| Защищённые Prometheus-метрики, request ID, error log и подписанный rate-limited alert webhook | готово | monitoring/API тесты |
| Пагинация пользовательских журналов, напоминаний, уведомлений и административных списков | готово | API-тесты offset/limit |
| Автоматическая очистка старых jobs, уведомлений, AI-логов, Telegram/billing событий и токенов | готово | retention-тест старых и свежих записей |
| TLS reverse proxy, TrustedHost, HSTS, body limit, container limits и log rotation | готово в конфигурации | API и статические deployment-тесты |
| Транзитивные lock-файлы production/dev с SHA-256; Docker/CI используют `--require-hashes` | готово | lock/deployment-тесты |
| Серверные ошибки LV/EN не содержат непереведённый русский текст | готово | AST completeness/fallback-тесты |
| Миграции Alembic 0001–0037 | готово | upgrade до head и downgrade до base |
| Expert eval: обязательные источники по причинам, taxonomy/code, provider failures, dataset hash, полный ответ и baseline gate | готово как инфраструктура | eval unit-тесты |

Итог последнего полного локального server-side прогона на чистом окружении из
`requirements-dev.lock`: **110 passed** за 291,81 с на `pytest 9.0.3`, включая полный
upgrade/downgrade миграций. Starlette TestClient переведён на `httpx2` без
deprecation-предупреждений. Ruff завершился без замечаний, а `pip-audit` для
production- и dev-lock не нашёл известных уязвимостей. JavaScript-файлы проверены через
`node --check`; Python и JSON — через parse/compile-проверку без создания кэшей.

## Внешние обязательные проверки перед публичным production-запуском

Это не отсутствующий код, а проверки, требующие внешних учётных данных или людей:

1. Агроном должен предоставить и подписать минимум 200 лицензированных случаев по
   правилам `evals/README.md`. До этого нельзя заявлять измеренную точность AI.
2. Выполнить `python -m evals.execute_evaluation --confirm-external-cost` с production
   OpenAI key и утвердить пороги метрик до включения диагностики для пользователей.
3. В staging проверить live-интеграции OpenAI, Stripe, Telegram и Open-Meteo с
   реальными секретами, webhook URL и политиками конкретных аккаунтов.
4. Дождаться успешного Docker smoke и PostgreSQL/pgvector migration job в CI/CD.
   Ruff и `pip-audit` уже прошли локально на окружении из lock-файлов; Docker в текущей
   локальной среде недоступен.
5. Провести юридическую проверку privacy/terms, лицензий источников и партнёрской
   рекламы для выбранных стран запуска.

## Команды контрольной проверки

```powershell
pip install --require-hashes -r requirements-dev.lock
alembic upgrade head
pytest -q
python evals/run_evaluation.py --validate-only
docker compose -f compose.prod.yaml config
```

Пустой `evals/cases.json` оставлен намеренно: выдуманная экспертная разметка была бы
опаснее честного блокирующего gate.

## Что ещё блокирует публичный коммерческий запуск

- Реализованы импорт версионированного нормализованного снимка VAAD/EU, контрольные
  суммы и автоматическое отключение рекомендаций по отозванной, истёкшей или
  отсутствующей записи. Автоматического скачивания пока нет: до него владелец продукта
  должен утвердить доступный официальный формат, лицензию повторного использования,
  расписание и процедуру сверки; снимок загружает ответственный специалист. EU API
  содержит действующие вещества и MRL, но не заменяет национальную проверку разрешения
  конкретного товара; у VAAD найден публичный список/PDF и веб-реестр, но не найден
  документированный открытый API реестра продуктов.
- B2B-тарифы, заявка/проверка конверсии, защита от двойного начисления, реестр счетов и
  неизменяемый операционный PDF, SMTP-отправка и точная сверка нормализованной банковской выгрузки реализованы. До production остаются юридическое и
  бухгалтерское утверждение налоговой нумерации/строк и порядка кредит-нот, e-invoice,
  утверждение формата банковского экспорта/live-коннектор и интеграция с бухгалтерией.
- Встроены request ID, Prometheus-метрики, журналирование ошибок и подписанный
  rate-limited alert webhook. До production нужно подключить их к выбранным внешним
  хранилищу метрик, error tracker и дежурному каналу, затем проверить тестовое оповещение.
- S3 private storage, короткие подписанные ссылки и CLI-аудит versioning, encryption,
  public-access block, lifecycle и чтения объектов реализованы. Фактические offsite-копии,
  provider-specific retention и restore drill должны быть настроены у выбранного
  S3-провайдера и испытаны в staging; PostgreSQL dump/verify/restore CLI готов для такого drill.
- Playwright Chromium E2E и axe WCAG gate проходят локально в Desktop Chrome и Pixel 5:
  **2 passed** за 41,5 с. Перед релизом тот же job должен пройти в чистом Linux-окружении;
  provider-specific визуальные отличия браузера остаются ответственностью CI.
- Обновлённые версии зависимостей закреплены в lock-файлах с SHA-256 и проверены в
  чистом локальном окружении: полный pytest, Ruff и `pip-audit` завершились успешно.
  CI должен повторить эти проверки в Linux и дополнительно выполнить Docker smoke.

До закрытия этих пунктов проект следует считать технически усиленным MVP/staging,
а не готовым публичным медицинско-агрономическим или коммерческим сервисом.

Чистый детерминированный release ZIP создаётся `scripts/package_release.py`: секреты,
локальные окружения, VCS-метаданные, БД, пользовательские загрузки и кэши исключаются,
а состав защищён встроенным SHA-256-манифестом.
