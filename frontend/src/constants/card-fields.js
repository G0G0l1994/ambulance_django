export const FIELD_TYPES = {
  INPUT: "input",
  TEXTAREA: "textarea",
  DATE: "dateInput",
  SELECT: "select",
};

export const patientData = [
  {
    name: "first_name",
    label: "Имя",
    type: FIELD_TYPES.INPUT,
    placeholder: "Введите имя пациента",
  },
  {
    name: "last_name",
    label: "Фамилия",
    type: FIELD_TYPES.INPUT,
    placeholder: "Введите фамилию пациента",
  },
  {
    name: "surname",
    label: "Отчество",
    type: FIELD_TYPES.INPUT,
    placeholder: "Введите отчество пациента",
  },
  {
    name: "date_of_birth",
    label: "Дата рождения",
    type: FIELD_TYPES.DATE,
    placeholder: "Введите дату рождения в формате ДД.ММ.ГГГГ",
  },
  {
    name: "address",
    label: "Адрес вызова",
    type: FIELD_TYPES.TEXTAREA,
    placeholder: "Введите адрес вызова",
  },
  {
    name: "cause",
    label: "Повод вызова",
    type: FIELD_TYPES.TEXTAREA,
    placeholder: "Введите повод вызова",
  },
];

export const CrewData = [
  {
    value: 101,
    label: "Бригада 101",
  },
  {
    value: 102,
    label: "Бригада 102",
  },
  {
    value: 103,
    label: "Бригада 103",
  },
];

export const StatusCard = [
  {
    value: "create",
    label: "Создана",
  },
  {
    value: "handed_crew",
    label: "Передана бригаде",
  },
  {
    value: "hospital",
    label: "Госпитализация",
  },
  {
    value: "completed",
    label: "Завершена",
  },
  {
    value: "cancelled",
    label: "Отменена",
  },
];
