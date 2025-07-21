import { VStack, Heading, Text, Button } from "@chakra-ui/react";
import { useEffect, useState } from "react";
import { getCardsList } from "../endpoints/api";

const CardsHistory = () => {
    const [cards, setCards] = useState([]);

    useEffect(() => {
        const fetchCards = async () => {
            const cardsData = await getCardsList();
            setCards(Array.isArray(cardsData) ? cardsData : []); // Если cardsData не массив, используем пустой массив
        };
        fetchCards();
    }, []);

    return (
        <VStack>
            <Heading>История вызовов</Heading>
            <VStack spacing={4} align="stretch" w="100%">
                {cards.map((card) => (
                    <VStack
                        key={card.id}
                        align="start"
                        borderWidth={1}
                        borderRadius="md"
                        p={4}
                    >
                        <Text>
                            <b>Пациент:</b> {card.patient?.full_name}{" "}
                            {card.patient?.date_of_birth &&
                                `(д.р. ${card.patient.date_of_birth})`}
                        </Text>
                        <Text>
                            <b>Бригада:</b> {card.crew}
                        </Text>
                        <Text>
                            <b>Причина:</b> {card.cause}
                        </Text>
                        <Text>
                            <b>Врач:</b> {card.doctor?.last_name}{" "}
                            {card.doctor?.first_name} {card.doctor?.surname}
                        </Text>
                        <Text>
                            <b>Статус:</b> {card.status}
                        </Text>
                        <Text key={card.diagnosis_data.id + "_mkb"}>
                            <b>МКБ-10:</b> {card.diagnosis_data["mkb"]}
                        </Text>
                        <Text key={card.diagnosis_data.id + "_diagnosis"}>
                            <b>Диагноз:</b> {card.diagnosis_data["diagnosis"]}
                        </Text>
                        <Button>Редактировать</Button>
                    </VStack>
                ))}
            </VStack>
        </VStack>
    );
};
export default CardsHistory;
