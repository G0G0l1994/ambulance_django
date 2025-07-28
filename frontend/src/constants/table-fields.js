export const columns = [
    {
        field: "id",
        label: "Номер карты",
    },
    {
        field: "last_name",
        label: "Фамилия",
    },
    {
        field: "first_name",
        label: "Имя",
    },
    {
        field: "surname",
        label: "Отчество",
    },
    {
        field: "date_of_birth",
        label: "Дата рождения",
    },
    {
        field: "address",
        label: "Адрес",
    },
    {
        field: "cause",
        label: "Повод",
    },
    {
        field: "crew",
        label: "Бригада",
    },
    {
        field: "status",
        label: "Статус",
    },
    {
        field: " ",
        label: " ",
    },
];

export const colorBackgroundStatus = {
    create: "blue.100",
    handed_crew: "green.100",
    cancelled: "red.100",
    completed: "green.100",
    // добавьте другие статусы по необходимости
};
