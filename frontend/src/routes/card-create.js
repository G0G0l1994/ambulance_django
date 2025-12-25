import { HStack, Input, VStack, Button } from "@chakra-ui/react";
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
    const year = data.slice(6);
    return `${year.join("")}-${month.join("")}-${days.join("")}`;
  };

  const handleDateChange = (e) => {
    const date = dateTransform(e.target.value);
    console.log(e.target.name);
    console.log(date);
    setFormData({ ...formData, [e.target.name]: date });
  };

  const handleSubmit = async () => {
    console.log(formData);
    try {
      const result = await cardCreate(formData);

      alert("Карта успешно создана");
      navigator("/dispatcher-main");
    } catch (error) {
      alert("Ошибка при создании карты");
      console.log(error.response.data);
    }
  };

  return (
    <VStack spacing={4}>
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
  );
};

export default CardPage;
