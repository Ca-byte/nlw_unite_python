# pass.in

Pass.in is an application for **managing participants in on-site events**.

The tool allows the organizer to register an event and create a public registration page.

Registered participants can generate a badge for check-in on the day of the event.

The system will scan the participant's badge to allow entry into the event.

## Requirements

### Functional Requirements

- [x] Organizer should be able to register a new event;
- [x] Organizer should be able to view event details;
- [x] Organizer should be able to view the list of participants;
- [x] Participant should be able to register for an event;
- [x] Participant should be able to view their registration badge;
- [x] Participant should be able to check-in to the event;

### Business Rules

- [x] A participant can only register for an event once;
- [x] A participant can only register for events with available slots;
- [x] A participant can only check-in to an event once;

### Non-Functional Requirements

- [x] Event check-in will be done using a QRCode;

## API Documentation (Swagger)

For the API documentation, visit the link: [API Documentation](https://nlw-unite-nodejs.onrender.com/docs)

## Database

In this application, we will use a relational database (SQL). For the development environment, we'll use SQLite due to its ease of use.

### ERD Diagram

![ERD Diagram of the database](.github/erd.svg)

### Database Structure (SQL)

```sql
-- CreateTable
CREATE TABLE "events" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "title" TEXT NOT NULL,
    "details" TEXT,
    "slug" TEXT NOT NULL,
    "maximum_attendees" INTEGER
);

-- CreateTable
CREATE TABLE "attendees" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "event_id" TEXT NOT NULL,
    "created_at" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "attendees_event_id_fkey" FOREIGN KEY ("event_id") REFERENCES "events" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "check_ins" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "created_at" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "attendeeId" INTEGER NOT NULL,
    CONSTRAINT "check_ins_attendeeId_fkey" FOREIGN KEY ("attendeeId") REFERENCES "attendees" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateIndex
CREATE UNIQUE INDEX "events_slug_key" ON "events"("slug");

-- CreateIndex
CREATE UNIQUE INDEX "attendees_event_id_email_key" ON "attendees"("event_id", "email");

-- CreateIndex
CREATE UNIQUE INDEX "check_ins_attendeeId_key" ON "check_ins"("attendeeId");
```