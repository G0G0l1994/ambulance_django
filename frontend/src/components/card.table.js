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

import { colorBackgroundStatus } from "../constants/table-fields";

export const CardTable = ({ columns, cards }) => {
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
                                background={bgColor}
                                key={card.id}
                                alignContent="center"
                            >
                                <Td>{card.id}</Td>
                                <Td>{card.patient.last_name}</Td>
                                <Td>{card.patient.first_name}</Td>
                                <Td>{card.patient.surname}</Td>
                                <Td>{card.patient.date_of_birth}</Td>
                                <Td>{card.address}</Td>
                                <Td>{card.cause}</Td>
                                <Td>{card.crew}</Td>
                                <Td>{card.status}</Td>
                                <Td>
                                    <Button>Редактировать</Button>
                                </Td>
                            </Tr>
                        );
                    })}
                </Tbody>
            </Table>
        </TableContainer>
    );
};
