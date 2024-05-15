const express = require('express')
const app = express()

const products = [
    {id: 1, name: 'Apel', image: 'https://res.cloudinary.com/dk0z4ums3/image/upload/v1630331723/attached_image/jarang-bertemu-dokter-berkat-manfaat-apel.jpg', description: 'Apel merupakan merupakan jenis buah-buahan, biasanya berwarna merah.', price: 15000, rating: 4.5},
    {id: 2, name: 'Pepaya', image: 'https://d1vbn70lmn1nqe.cloudfront.net/prod/wp-content/uploads/2022/01/19025309/Ragam-Manfaat-Pepaya-California-yang-Jarang-Diketahui-01-1.jpg', description: 'Pepaya merupakan merupakan jenis buah-buahan, berwarna hijau.', price: 12000, rating: 4.5},
    {id: 3, name: 'Mangga', image: 'https://akcdn.detik.net.id/visual/2021/07/06/ilustrasi-mangga_169.jpeg?w=650', description: 'Mangga merupakan merupakan jenis buah-buahan, biasanya berwarna hijau.', price: 20000, rating: 4.5}
]


app.get('/products', (req, res) => {
    res.json(products)
})

app.get('/products/:product_id', (req, res) => {
    const productId = parseInt(req.params.product_id)
    const product = products.find(product => product.id === productId)

    if(product){
        res.json(product);
    }else {
        res.status(404).json('Product not found.')
    }
})

app.listen(5000, () =>{
    console.log('server berjalan')
})