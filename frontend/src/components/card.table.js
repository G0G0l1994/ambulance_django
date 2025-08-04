import {
    TableContainer,
    Table,
    Thead,
    Th,
    Tr,
    Tbody,
    Td,
    Button,
} from "@chakra-ui/react";

import { useNavigate } from "react-router-dom";
import { colorBackgroundStatus } from "../constants/table-fields";
import { Link } from "react-router-dom";

export const CardTable = ({ columns, cards }) => {
    const navigator = useNavigate();
    return (
        <TableContainer>
            <Table variant="simple">
                <Thead>
                    <Tr>
                        {columns.map((col) => {
                            return <Th key={col.field}>{col.label} </Th>;
                        })}
                    </Tr>
                </Thead>
                <Tbody>
                    {cards.map((card) => {
                        const bgColor =
                            colorBackgroundStatus[card.status] || "grey.100";
                        return (
                            <Tr
                                bg={bgColor}
                                key={card.id}
                                _hover={{ bg: "gray.100", cursor: "pointer" }}
                            >
                                {/* Ячейки с данными */}
                                <Td
                                    onClick={() =>
                                        navigator(`/cards/${card.id}`)
                                    }
                                >
                                    {card.id}
                                </Td>
                                <Td
                                    onClick={() =>
                                        navigator(`/cards/${card.id}`)
                                    }
                                >
                                    {card.patient.last_name}
                                </Td>
                                <Td
                                    onClick={() =>
                                        navigator(`/cards/${card.id}`)
                                    }
                                >
                                    {card.patient.first_name}
                                </Td>
                                <Td
                                    onClick={() =>
                                        navigator(`/cards/${card.id}`)
                                    }
                                >
                                    {card.patient.surname}
                                </Td>
                                <Td
                                    onClick={() =>
                                        navigator(`/cards/${card.id}`)
                                    }
                                >
                                    {card.patient.date_of_birth}
                                </Td>
                                <Td
                                    onClick={() =>
                                        navigator(`/cards/${card.id}`)
                                    }
                                >
                                    {card.address}
                                </Td>
                                <Td
                                    onClick={() =>
                                        navigator(`/cards/${card.id}`)
                                    }
                                >
                                    {card.cause}
                                </Td>
                                <Td
                                    onClick={() =>
                                        navigator(`/cards/${card.id}`)
                                    }
                                >
                                    {card.crew}
                                </Td>
                                <Td
                                    onClick={() =>
                                        navigator(`/cards/${card.id}`)
                                    }
                                >
                                    {card.status}
                                </Td>

                                {/* Отдельная ячейка для кнопки редактирования */}
                                <Td>
                                    <Button
                                        onClick={(e) => {
                                            e.stopPropagation();
                                            navigator(
                                                `/cards/${card.id}/update`
                                            );
                                        }}
                                    >
                                        Редактировать
                                    </Button>
                                </Td>
                            </Tr>
                        );
                    })}
                </Tbody>
            </Table>
        </TableContainer>
    );
};
