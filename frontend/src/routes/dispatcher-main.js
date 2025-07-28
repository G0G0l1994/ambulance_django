import { useState, useEffect } from "react";
import { VStack, Heading, Button } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";
import { Text } from "@chakra-ui/react";
import { getCardsList } from "../endpoints/api";
import { columns } from "../constants/table-fields";
import { CardTable } from "../components/card.table";

const DispatcherMain = () => {
    const [cards, setCards] = useState([]);

    useEffect(() => {
        const fetchCards = async () => {
            const cardsData = await getCardsList();
            setCards(Array.isArray(cardsData) ? cardsData : []); // Если cardsData не массив, используем пустой массив
        };
        fetchCards();
    }, []);
    console.log(cards);
    return (
        <VStack>
            <Heading> Диспетчерская </Heading>
            <VStack spacing={4} align="stretch" w="100%">
                <CardTable columns={columns} cards={cards} />
            </VStack>
        </VStack>
    );
};

export default DispatcherMain;
