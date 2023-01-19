import { getAllPages } from "nextra/context"

export function AllRoutes() {
    console.log(getAllPages())
    console.log(JSON.stringify(getAllPages()))
    return <></>
}