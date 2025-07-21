import { HStack, Input, VStack, Button } from "@chakra-ui/react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import {
    InputTextField,
    InputField,
    DateField,
} from "../components/cards.text.field";
import { SelectChoice } from "../components/choice.field";

import { patientData, FIELD_TYPES, CrewData } from "../constants/card-fields";
import { cardCreate } from "../endpoints/api";

const CardPage = () => {
    const [formData, setFormData] = useState({ status: "create" });
    const navigator = useNavigate();
    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async () => {
        try {
            const result = await cardCreate(formData);
            alert("Карта успешно создана");
            console.log(formData);
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
                            onChange={handleChange}
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

            {/* <SelectChoice
                options={CrewData}
                name="crew"
                fieldname="Номер Бригады"
                onChange={handleChange}
                placeholder="Выбор бригады"
            /> */}
            <Button colorScheme="blue" onClick={handleSubmit}>
                Создать карту
            </Button>
        </VStack>
    );
};

export default CardPage;
