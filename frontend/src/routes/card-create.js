import { HStack, Input, VStack, Button, Grid } from "@chakra-ui/react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  InputTextField,
  InputField,
  DateField,
} from "../components/fields/cards.text.field";
import { SelectChoice } from "../components/fields/choice.field";

import { patientData, FIELD_TYPES, CrewData } from "../constants/card-fields";
import { cardCreate } from "../endpoints/api";

const CardPage = () => {
  const [formData, setFormData] = useState({ status: "create" });
  const navigator = useNavigate();
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };
  const dateTransform = (date) => {
    const data = Array.from(date);
    const days = data.slice(0, 2);
    const month = data.slice(3, 5);
    const year = data.slice(6, 10);

    return `${year.join("")}-${month.join("")}-${days.join("")}`;
  };

  const handleDateChange = (e) => {
    const date = dateTransform(e.target.value);
    setFormData({ ...formData, [e.target.name]: date });
  };

  const handleSubmit = async () => {
    try {
      await cardCreate(formData);
      alert("Карта успешно создана");
      navigator("/dispatcher-main");
    } catch (error) {
      alert(
        `Ошибка при создании карты: ${JSON.stringify(error.response.data)}`
      );
    }
  };

  return (
    <Grid gap={5} templateColumns="repeat(1, 1fr)">
      <VStack p={2}>
        {patientData.map((field) => {
          if (field.type === FIELD_TYPES.INPUT) {
            return (
              <InputField
                key={field.name}
                fieldname={field.label}
                placeholder={field.placeholder}
                name={field.name}
                onChange={handleChange}
              />
            );
          }
          if (field.type === FIELD_TYPES.DATE) {
            return (
              <DateField
                key={field.name}
                fieldname={field.label}
                placeholder={field.placeholder}
                name={field.name}
                onChange={handleDateChange}
                align="start"
              />
            );
          }
          if (field.type === FIELD_TYPES.TEXTAREA) {
            return (
              <InputTextField
                key={field.name}
                fieldname={field.label}
                placeholder={field.placeholder}
                name={field.name}
                onChange={handleChange}
              />
            );
          }
        })}
        <Button colorScheme="blue" onClick={handleSubmit}>
          Создать карту
        </Button>
      </VStack>
    </Grid>
  );
};

export default CardPage;
